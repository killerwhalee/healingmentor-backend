from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    ValidationError,
)

from session.utils import calculate_score
from session.models import (
    GuidedMeditation,
    RespiratoryGraph,
    SustainedAttention,
)
from session.serializer import (
    GuidedMeditationSerializer,
    RespiratoryGraphSerializer,
    SustainedAttentionSerializer,
)


class SessionViewSet(viewsets.ViewSet):
    """
    ### Base Session Viewset

    This is base session viewset.

    You can use custom-defined session model and serializer by setting
    `Session` and `SessionSerializer` to your session model and serializer.

    """

    Session = None
    SessionSerializer = None

    def list(self, request):
        session_list = self.Session.objects.filter(user=request.user)
        serializer = self.SessionSerializer(session_list, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        serializer = self.SessionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["user"] = request.user
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        raise ValidationError(detail=serializer.errors)

    def retrieve(self, request, session_id):
        try:
            session = self.Session.objects.get(id=session_id)

            if request.user == session.user:
                serializer = self.SessionSerializer(session)

                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK,
                )

            raise PermissionDenied(
                detail="You do not have permission to access this object",
                code="access_denied",
            )

        except ObjectDoesNotExist:
            raise NotFound(
                detail="Object does not exist",
                code="not_found",
            )

    def destroy(self, request, session_id):
        try:
            session = self.Session.objects.get(id=session_id)

            if request.user == session.user:
                session.delete()

                return Response(
                    status=status.HTTP_204_NO_CONTENT,
                )

            raise PermissionDenied(
                detail="You do not have permission to access this object",
                code="access_denied",
            )

        except ObjectDoesNotExist:
            raise NotFound(
                detail="Object does not exist",
                code="not_found",
            )


class GuidedMeditationViewSet(SessionViewSet):
    Session = GuidedMeditation
    SessionSerializer = GuidedMeditationSerializer


class RespiratoryGraphViewSet(SessionViewSet):
    Session = RespiratoryGraph
    SessionSerializer = RespiratoryGraphSerializer


class SustainedAttentionViewSet(SessionViewSet):
    Session = SustainedAttention
    SessionSerializer = SustainedAttentionSerializer
