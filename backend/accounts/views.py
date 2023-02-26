import logging

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserRegistrationSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserRegisterView(CreateModelMixin, GenericAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = ()

    def post(self, request):
        """User registration view."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.create(request)
            return Response(status=status.HTTP_201_CREATED)
        logger.warning(f"User Register Error {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOwnAccountView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"user": self.get_serializer(request.user).data})
