from rest_framework import serializers
from server.models import Venue, UserProfile, Gang
from django.contrib.auth.models import User


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'user', 'latitude', 'longitude', 'latestEditTimestamp', 'category')

class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.Field(source = 'user.username')

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'username','latitude', 'longitude', 'tagsCreated', 'tagsDeleted', 'money', 'gang')


class GangSerializer(serializers.ModelSerializer):
    gangsters = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('id', 'name', 'gangsters')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')