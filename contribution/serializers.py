from rest_framework import serializers
from .models import Group, UserGroup, Contribution
from django.contrib.auth.models import User

# Group Serializer
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name', 'amount', 'capacity', 'admin', 'isPublic', 'description')


# User's Group's Serializer
class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('group', 'user', 'slot', 'saving', 'expense')

# Contribution Serializer
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('amount', 'source', 'destination')