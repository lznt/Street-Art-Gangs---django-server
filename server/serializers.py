from rest_framework import serializers
from server.models import Venue, UserProfile
from django.contrib.auth.models import User


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'latitude', 'longitude')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
