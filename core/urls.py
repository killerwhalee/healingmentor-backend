from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin Page
    path("admin/", admin.site.urls),
    # API Endpoints
    path("api/v1/user/", include("user.urls")),
    path("api/v1/session/", include("session.urls")),
    path("api/v1/board/", include("board.urls")),
]

# Generic JSON Error Views
handler400 = "core.exceptions.bad_request"
handler404 = "core.exceptions.page_not_found"
handler500 = "core.exceptions.server_error"
