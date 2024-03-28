from django.contrib.auth import authenticate

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import (
    AuthenticationFailed,
)

from rest_framework_simplejwt.tokens import RefreshToken

from user.serializer import (
    UserAuthSerializer,
    UserSerializer,
    ProfileSerializer,
)


class UserAuthViewSet(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

    def login(self, request):
        serializer = UserAuthSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.data["username"]
            password = serializer.data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            serializer = UserAuthSerializer(user)
            refresh = RefreshToken.for_user(user)

            return Response(
                data={
                    "user": serializer.data["username"],
                    "token": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                    },
                },
                status=status.HTTP_200_OK,
            )

        raise AuthenticationFailed(
            detail="Wrong username or password",
        )

    def signup(self, request):
        serializer = UserAuthSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            serializer = UserAuthSerializer(user)
            refresh = RefreshToken.for_user(user)

            return Response(
                data={
                    "user": serializer.data["username"],
                    "token": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                    },
                },
                status=status.HTTP_200_OK,
            )

        raise AuthenticationFailed(
            detail="Failed to sign up",
        )


class ProfileViewSet(viewsets.ViewSet):
    def retrieve(self, request):
        serializer = ProfileSerializer(request.user.profile)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def update(self, request):
        pass

    def destroy(self, request):
        pass
