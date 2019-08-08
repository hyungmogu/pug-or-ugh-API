from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404
from rest_framework import permissions, mixins, viewsets
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
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserDogSerializer

    def get_object(self):
        dog = get_object_or_404(models.Dog, pk=self.kwargs.get('pk'))
        print(dog)
        print('!!!!!!')
        print('hello')
        try:
            obj = self.model.objects.get(user=self.request.user, dog=dog)
        except self.model.DoesNotExist:
            obj = self.model.objects.create(user=self.request.user, dog=dog)
        return obj