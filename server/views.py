#Base
from rest_framework import viewsets

#Authentication and Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#Models
from server.models import Venue, UserProfile, Gang
from django.contrib.auth.models import User

#Serializers
from server.serializers import VenueSerializer, UserProfileSerializer, GangSerializer, UserSerializer

class VenueViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
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
