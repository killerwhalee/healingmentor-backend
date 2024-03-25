from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserAuthViewSet, ProfileViewSet

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
        ProfileViewSet.as_view({"get": "retrieve", "patch": "update"}),
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(),
    ),
]
