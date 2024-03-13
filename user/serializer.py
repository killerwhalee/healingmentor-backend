from rest_framework import serializers

from user.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["object", "id", "username"]
        read_only_fields = ["object", "id"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        
        return user

    def get_object(self, _):
        return "user"


class ProfileSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["object", "id", "user", "date_joined", "profile_image"]
        read_only_fields = ["object", "id", "date_joined"]

    def get_object(self, _):
        return "profile"
