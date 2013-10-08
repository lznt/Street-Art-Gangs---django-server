from django.forms import widgets
from rest_framework import serializers
from server.models import User, Team, Venue


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('name')

