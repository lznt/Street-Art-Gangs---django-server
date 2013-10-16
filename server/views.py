from server.serializers import VenueSerializer, UserProfileSerializer
from server.models import Venue
from django.contrib.auth.models import User
from rest_framework import viewsets


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
