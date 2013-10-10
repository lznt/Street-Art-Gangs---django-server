from server.serializers import GangSerializer, GangsterSerializer
from rest_framework import generics
from server.models import Venue, Gang, Gangster
from rest_framework import permissions




class GangsterList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gangster.objects.all()
    serializer_class = GangsterSerializer


class GangsterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Gangster.objects.all()
    serializer_class = GangsterSerializer


class GangList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gang.objects.all()
    serializer_class = GangSerializer


class GangDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gang.objects.all()
    serializer_class = GangSerializer
