from django.contrib.auth.models import Group, User
from server.serializers import TeamSerializer
from rest_framework import generics


class GangList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GangSerializer


class GangDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GangSerializer
