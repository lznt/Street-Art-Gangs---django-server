from server.serializers import VenueSerializer
from server.models import Venue
from rest_framework import viewsets


class VenueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
