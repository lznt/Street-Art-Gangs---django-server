from rest_framework import serializers
from server.models import Venue, UserProfile
from django.contrib.auth.models import User


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'user', 'latitude', 'longitude', 'latestEditTimestamp', 'category')

class UserProfileSerializer(serializers.ModelSerializer):

    username = serializers.Field(source = 'user.username')

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'username','latitude', 'longitude', 'tagsCreated', 'tagsDeleted', 'money')
