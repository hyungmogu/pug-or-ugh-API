from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

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

class UpdateDogView(UpdateAPIView):
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
        dog_pk = self.kwargs.get('pk')
        user_pk = request.user.pk
        status_type = self.kwargs.get('type')
        dog = get_object_or_404(models.Dog, pk=dog_pk)

        if status_type == 'liked':
            req_status = 'l'
        elif status_type == 'disliked':
            req_status = 'd'
        elif status_type == 'undecided':
            req_status = ''

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


class RetrieveNextDogView(RetrieveAPIView):
    model = models.Dog
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.DogSerializer

    def get_object(self):
        pk = int(self.kwargs.get('pk'))
        status_type = self.kwargs.get('type')

        if status_type == 'liked':
            status = 'l'
        elif status_type == 'disliked':
            status = 'd'
        elif status_type == 'undecided':
            status = ''

        if not pk:
            raise NotFound

        temp_obj = models.UserDog.objects \
                    .filter(Q(user=self.request.user)&Q(status=status)&Q(dog__pk__gt=self.kwargs.get('pk'))) \
                    .select_related('dog').first()

        if not temp_obj:
            raise NotFound

        obj = temp_obj.dog

        return obj