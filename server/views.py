from server.serializers import VenueSerializer, UserSerializer
from server.models import Venue
from django.contrib.auth.models import User
from rest_framework import viewsets


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
