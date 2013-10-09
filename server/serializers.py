from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster


class GangSerializer(serializers.ModelSerializer):

    name = serializers.SlugRelatedField(slug_field='name')
    gangsters = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('name', 'gangsters')


class GangsterSerializer(serializers.ModelSerializer):

    username = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = Gangster
        fields = ('username','gang')



class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

