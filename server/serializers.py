from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster


class GangSerializer(serializers.ModelSerializer):

    gangsters = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('group', 'gangsters')
        depth = 1


class GangsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gangster
        fields = ('user','gang')
        depth = 1


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

