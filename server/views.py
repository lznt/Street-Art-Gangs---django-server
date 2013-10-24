#Base
from rest_framework import viewsets
from rest_framework import generics

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
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GangViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Gang.objects.all()
    serializer_class = GangSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserRegistrerView(generics.GenericAPIView):

    """
    Create a new User.
    """

    def get(self, request, *args, **kwargs):

        # GET not allowed
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)



    def post(self, request, format=None):
        user_profile_serializer = UserProfileSerializer(
                data=request.DATA)
        user_serializer = UserSerializer(
                data=request.DATA)
        if user_profile_serializer.is_valid() and user_serializer.is_valid():
            user_serializer.save()
            user_profile_serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Combine errors from both serializers.
        errors = dict()
        errors.update(user_profile_serializer.errors)
        errors.update(user_serializer.errors)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
