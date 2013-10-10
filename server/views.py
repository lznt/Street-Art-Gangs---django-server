from server.serializers import GangSerializer, GangsterSerializer
from rest_framework import generics
from server.models import Venue, Gang, Gangster
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class GangsterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gangster.objects.all()
    serializer_class = GangsterSerializer


class GangViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gang.objects.all()
    serializer_class = GangSerializer
