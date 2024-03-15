from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserAuthViewSet, UserViewSet

urlpatterns = [
    path(
        "auth/login",
        UserAuthViewSet.as_view({"post": "login"}),
    ),
    path(
        "auth/signup",
        UserAuthViewSet.as_view({"post": "signup"}),
    ),
    path(
        "profile",
        UserViewSet.as_view({"get": "retrieve", "patch": "update"}),
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(),
    ),
]
