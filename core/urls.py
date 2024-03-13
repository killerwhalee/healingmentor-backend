from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin Page
    path("admin/", admin.site.urls),
    # API Endpoints
    path("api/v1/user/", include("user.urls")),
    path("api/v1/session/", include("session.urls")),
]
