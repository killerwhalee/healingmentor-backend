from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets
from rest_framework.response import Response

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

        return Response(serializer.data)

    def create(self, request):
        serializer = self.SessionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["user"] = request.user
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def retrieve(self, request, session_id):
        try:
            session = self.Session.objects.get(id=session_id)

            if request.user == session.user:
                serializer = self.SessionSerializer(session)

                return Response(serializer.data)

            return Response(
                {
                    "error": "access_denied",
                    "message": "You do not have permission to access this object",
                },
                status=403,
            )

        except ObjectDoesNotExist:
            return Response(
                {
                    "error": "not_found",
                    "message": "Object does not exist",
                },
                status=404,
            )

    def destroy(self, request, session_id):
        try:
            session = self.Session.objects.get(id=session_id)

            if request.user == session.user:
                session.delete()

                return Response(status=204)

            return Response(
                {
                    "error": "access_denied",
                    "message": "You do not have permission to access this object",
                },
                status=403,
            )

        except ObjectDoesNotExist:
            return Response(
                {
                    "error": "not_found",
                    "message": "Object does not exist",
                },
                status=404,
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
