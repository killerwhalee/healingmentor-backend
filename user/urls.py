from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from user.views import AuthViewSet, UserViewSet

urlpatterns = [
    path(
        "auth/login",
        AuthViewSet.as_view({"post": "login"}),
    ),
    path(
        "auth/signup",
        AuthViewSet.as_view({"post": "signup"}),
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
