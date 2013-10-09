from django.forms import widgets
from rest_framework import serializers
from server.models import Venue
from django.contrib.auth.models import Group, User


class GangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class GangsterSerializer(serializers.ModelSerializer):
    gang = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = User
        fields = ('id','username', 'gang')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')
