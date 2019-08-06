from django.contrib.auth import get_user_model

from rest_framework import permissions, mixins, viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

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
        return self.model.objects.get(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(user=user)

