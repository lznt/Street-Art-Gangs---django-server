from django.forms import widgets
from rest_framework import serializers
from server.models import Venue, Gang, Gangster
from django.contrib.auth.models import Group, User

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class GangSerializer(serializers.ModelSerializer):

    group = GroupSerializer()
    gangsters = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Gang
        fields = ('group', 'gangsters')


class GangsterSerializer(serializers.ModelSerializer):

    gang = GangSerializer()
    user = UserSerializer()

    class Meta:
        model = Gangster
        fields = ('user','gang')



class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id','name')

