from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang
from django.contrib.auth.models import Group, User


class GangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gang
        fields = ('group.id', 'group.name')


class GangsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gangster
        fields = ('user.id','user.username')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

