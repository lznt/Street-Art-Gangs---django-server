from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster


class GangSerializer(serializers.ModelSerializer):

    gangs = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('group', 'gangsters')


class GangsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gangster


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

