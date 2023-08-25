from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from accounts.serializers import UserSerializer


class AccountCreateRetrieveViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"detail": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        user.is_register = True
        user.save()
        return Response(data=serializer.data)