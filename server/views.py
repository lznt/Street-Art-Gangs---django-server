from django.contrib.auth.models import Group, User
from server.serializers import GangSerializer, GangsterSerializer
from rest_framework import generics


class GangsterList(generics.ListCreateAPIView):
    queryset = Gangster.objects.all()
    serializer_class = GangsterSerializer


class GangsterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gangster.objects.all()
    serializer_class = GangsterSerializer


class GangList(generics.ListCreateAPIView):
    queryset = Gang.objects.all()
    serializer_class = GangSerializer


class GangDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gang.objects.all()
    serializer_class = GangSerializer
