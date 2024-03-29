from rest_framework import serializers

from board.models import Post
from user.serializer import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = [
            "object",
            "id",
            "user",
            "date_created",
            "last_update",
        ]

    def get_object(self, _):
        return "post"