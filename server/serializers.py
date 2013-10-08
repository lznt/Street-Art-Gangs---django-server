from django.forms import widgets
from rest_framework import serializers
from server.models import User, Team, Venue



class TeamSerializer(serializers.Serializer):

    pk = serializers.Field()
    name = serializers.CharField(max_length=100)



class UserSerializer(serializers.Serializer):

    pk = serializers.Field()
    nickname = serializers.CharField(max_length=100)
