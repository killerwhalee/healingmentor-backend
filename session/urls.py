from django.urls import path

from session.views import (
    GuidedMeditationViewSet,
    RespiratoryGraphViewSet,
    SustainedAttentionViewSet,
)


urlpatterns = [
    path(
        "gm",
        GuidedMeditationViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "gm/<uuid:session_id>",
        GuidedMeditationViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
    ),
    path(
        "rg",
        RespiratoryGraphViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "rg/<uuid:session_id>",
        RespiratoryGraphViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
    ),
    path(
        "sa",
        SustainedAttentionViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "sa/<uuid:session_id>",
        SustainedAttentionViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
    ),
]
