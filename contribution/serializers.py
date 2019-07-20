from rest_framework import serializers
from .models import Group, UserGroup, Contribution
from django.contrib.auth.models import User

# Group Serializer
class GroupSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ["name", "amount", "slots", "users", "isActive"]

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = "__all__"

# User's Group's Serializer
class UserGroupSerializer(serializers.ModelSerializer):
    credits = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    debits = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = UserGroup
        fields = "__all__"

# Contribution Serializer
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = "__all__"