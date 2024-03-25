from rest_framework import serializers

from session.models import (
    GuidedMeditation,
    RespiratoryGraph,
    SustainedAttention,
)
from user.serializer import UserSerializer


class GuidedMeditationSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = GuidedMeditation
        fields = "__all__"
        read_only_fields = [
            "object",
            "id",
            "user",
            "date_created",
            "last_update",
            "score",
        ]

    def get_object(self, _):
        return "session"


class RespiratoryGraphSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = RespiratoryGraph
        fields = "__all__"
        read_only_fields = [
            "object",
            "id",
            "user",
            "date_created",
            "last_update",
            "score",
        ]

    def get_object(self, _):
        return "session"


class SustainedAttentionSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = SustainedAttention
        fields = "__all__"
        read_only_fields = [
            "object",
            "id",
            "user",
            "date_created",
            "last_update",
            "score",
        ]

    def get_object(self, _):
        return "session"
