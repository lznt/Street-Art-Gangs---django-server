from rest_framework import serializers
from server.models import Venue

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'latitude', 'longitude')
