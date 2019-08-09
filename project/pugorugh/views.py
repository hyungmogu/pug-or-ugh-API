from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView

from . import serializers
from . import models


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = serializers.UserSerializer

class UserPerfView(RetrieveUpdateAPIView):
    model = models.UserPerf
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserPerfSerializer

    def get_object(self):
        try:
            obj = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            obj = self.model.objects.create(user=self.request.user)

        return obj

class RetrieveDogView(RetrieveAPIView):
    queryset = models.Dog.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.DogSerializer


class RetrieveUpdateDogLikeView(UpdateAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def get_object(self):
        dog = get_object_or_404(models.Dog, pk=self.kwargs.get('pk'))
        try:
            obj = self.model.objects.get(user=self.request.user, dog=dog)
        except self.model.DoesNotExist:
            obj = self.model.objects.create(user=self.request.user, dog=dog)
        return obj

    def update(self, request, *args, **kwargs):

        # update object
        dog_pk = self.kwargs.get('pk')
        user_pk = request.user.pk
        req_status = 'l'
        dog = get_object_or_404(models.Dog, pk=dog_pk)

        try:
            user_dog = self.model.objects.get(user=request.user, dog=dog)
        except self.model.DoesNotExist:
            user_dog = self.model.objects.create(user=request.user, dog=dog)

        serializer = self.serializer_class(user_dog, data={
            "dog": dog_pk,
            "user": user_pk,
            "status": req_status
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        # use serializer to retrieve user dog object in JSON data format
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDogDislikeView(UpdateAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def get_object(self):
        dog = get_object_or_404(models.Dog, pk=self.kwargs.get('pk'))
        try:
            obj = self.model.objects.get(user=self.request.user, dog=dog)
        except self.model.DoesNotExist:
            obj = self.model.objects.create(user=self.request.user, dog=dog)
        return obj

    def update(self, request, *args, **kwargs):

        # update object
        dog_pk = self.kwargs.get('pk')
        user_pk = request.user.pk
        req_status = 'd'
        dog = get_object_or_404(models.Dog, pk=dog_pk)

        try:
            user_dog = self.model.objects.get(user=request.user, dog=dog)
        except self.model.DoesNotExist:
            user_dog = self.model.objects.create(user=request.user, dog=dog)

        serializer = self.serializer_class(user_dog, data={
            "dog": dog_pk,
            "user": user_pk,
            "status": req_status
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        # use serializer to retrieve user dog object in JSON data format
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveUpdateDogUndecidedView(UpdateAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def get_object(self):
        dog = get_object_or_404(models.Dog, pk=self.kwargs.get('pk'))
        try:
            obj = self.model.objects.get(user=self.request.user, dog=dog)
        except self.model.DoesNotExist:
            obj = self.model.objects.create(user=self.request.user, dog=dog)
        return obj

    def update(self, request, *args, **kwargs):

        # update object
        dog_pk = self.kwargs.get('pk')
        user_pk = request.user.pk
        req_status = ''
        dog = get_object_or_404(models.Dog, pk=dog_pk)

        try:
            user_dog = self.model.objects.get(user=request.user, dog=dog)
        except self.model.DoesNotExist:
            user_dog = self.model.objects.create(user=request.user, dog=dog)

        serializer = self.serializer_class(user_dog, data={
            "dog": dog_pk,
            "user": user_pk,
            "status": req_status
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        # use serializer to retrieve user dog object in JSON data format
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveDogNextLikeView(RetrieveAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.model.objects.filter(Q(user=request.user)&Q(status='l')&Q(dog__pk__gt=self.kwargs.get('pk'))).first()

        if not obj:
            raise NotFound

        serializer = self.serializer_class(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveDogNextDislikeView(RetrieveAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.model.objects.filter(Q(user=request.user)&Q(status='d')&Q(dog__pk__gt=self.kwargs.get('pk'))).first()

        if not obj:
            raise NotFound

        serializer = self.serializer_class(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveDogNextUndecidedView(RetrieveAPIView):
    model = models.UserDog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.model.objects.filter(Q(user=request.user)&Q(status='')&Q(dog__pk__gt=self.kwargs.get('pk'))).first()

        if not obj:
            raise NotFound

        serializer = self.serializer_class(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
