from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster


class GangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gang


class GangsterSerializer(serializers.ModelSerializer):
    gang = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gangster
        fields = ('user', 'gang')

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

