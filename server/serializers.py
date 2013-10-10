from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster
from django.contrib.auth.models import Group, User



class GangSerializer(serializers.ModelSerializer):

    name = serializers.Field(source = 'group.name')
    #gangsters = serializers.PrimaryKeyRelatedField(many=True)
    gangsters = GangsterSerializer(many=True)
    class Meta:
        model = Gang
        fields = ('name', 'gangsters')


class GangsterSerializer(serializers.ModelSerializer):

    gang = serializers.Field(source = 'gang.group.name')
    username = serializers.Field(source = 'user.username')


    class Meta:
        model = Gangster
        fields = ('username','gang')



class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

