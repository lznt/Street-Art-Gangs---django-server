from rest_framework import serializers
from server.models import Venue
from django.contrib.auth.models import User


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'latitude', 'longitude')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
