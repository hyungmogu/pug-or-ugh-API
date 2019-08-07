from django.contrib.auth import get_user_model

from rest_framework import permissions, mixins, viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView

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
