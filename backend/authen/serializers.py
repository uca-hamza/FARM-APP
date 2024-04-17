from rest_framework import serializers
from .models import (
    CustomUser,
    ProfileProgress,
)

# Serializers for User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "name", "lastname", "matricule", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
# Serializers for ProfileProgress
class ProfileProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileProgress
        fields = "__all__"
        extra_kwargs = {"id_user": {"read_only": True}}