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

        user_perf = models.UserPerf.objects.get(user=self.request.user)

        temp_user_perf_size = [x for x in user_perf.size.split(',')]
        user_perf_size = r'({0})'.format('|'.join(temp_user_perf_size))

        temp_user_perf_gender = [x for x in user_perf.gender.split(',')]
        user_perf_gender = r'({0})'.format('|'.join(temp_user_perf_gender))

        result = models.UserDog.objects \
                    .filter(
                        Q(user=self.request.user)&
                        Q(status=status)&
                        Q(dog__gender__iregex=user_perf_gender)&
                        Q(dog__size__iregex=user_perf_size)&
                        Q(dog__pk__gt=self.kwargs.get('pk'))
                    )

        if 'b' not in user_perf.age:
            result = result.exclude(Q(dog__age__lt=11))

        if 'y' not in user_perf.age:
            result = result.exclude(Q(dog__age__gte=11)&Q(dog__age__lt=20))

        if 'a' not in user_perf.age:
            result = result.exclude(Q(dog__age__gte=20)&Q(dog__age__lt=60))

        if 's' not in user_perf.age:
            result = result.exclude(Q(dog__age__gte=60))

        obj = result.select_related('dog').first()

        if not obj:
            raise NotFound

        obj = obj.dog

        return obj