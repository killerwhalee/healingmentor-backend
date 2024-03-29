from django.urls import path

from board.views import BoardViewSet


urlpatterns = [
    path(
        "",
        BoardViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<uuid:post_id>",
        BoardViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
    ),
]
