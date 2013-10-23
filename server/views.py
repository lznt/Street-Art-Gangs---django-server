from server.serializers import VenueSerializer, UserProfileSerializer, GangSerializer
from server.models import Venue, UserProfile, Gang
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GangViewSet(viewsets.ModelViewSet):
    queryset = Gang.objects.all()
    serializer_class = GangSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


