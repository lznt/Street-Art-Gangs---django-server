from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster


class GangSerializer(serializers.ModelSerializer):

    gangsters = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('group.id','group.name', 'gangsters')


class GangsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gangster
        fields = ('user.id','user.username', 'gang.group.name')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

