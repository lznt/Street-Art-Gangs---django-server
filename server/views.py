from server.serializers import VenueSerializer, UserProfileSerializer
from server.models import Venue, UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import CreateAPIView
from rest_framework.response import Response
from rest_framework import status



class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

"""
class Registration(CreateAPIView):

    def post(self, request):

        Accepts a JSON request containing:
            - username
            - email
            - password
        and saves the User on the backend

        try:
            data = request.DATA
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        username = force_unicode(data.get('username',''))
        email = force_unicode(data.get('email',''))
        password = force_unicode(data.get('password',''))

        if username == '' or email == '' or password == '':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            User.objects.get(username=username)
            return Response(status=HTTP_409_CONFLICT)
        except User.DoesNotExist:
            User.objects.create_user(username,email,password)
            return Response(status=HTTP_201_CREATED)
"""
