#Base
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

	def list(self, request):
		queryset = UserProfile.objects.filter(acted_recently = True)
		serializer = UserProfileSerializer(queryset, many=True)
		return Response(serializer.data)

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


class UserAuthView(APIView):

	#Login. Returns the current user.
	def get(self, request, *args, **kwargs):
		# Only UserProfileSerializer is required to serialize data since
		# email is populated by the 'source' param on EmailField.
		if (request.user.is_authenticated()):
			serializer = UserProfileSerializer(
					instance=request.user.profile)
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(status=status.HTTP_401_UNAUTHORIZED)


	#Register new user.
	def post(self, request, format=None):
		user_serializer = UserSerializer(data=request.DATA)
		errors = dict()
		if user_serializer.is_valid():
			user =user_serializer.save()
			data = request.DATA.copy()
			data['user'] = User.objects.latest('id').id
			user_profile_serializer = UserProfileSerializer(data=data)

			if user_profile_serializer.is_valid():
				user_profile_serializer.save()
				return Response(user_profile_serializer.data, status=status.HTTP_201_CREATED)

			errors.update(user_profile_serializer.errors)
			return Response(errors, status=status.HTTP_400_BAD_REQUEST)


		errors.update(user_serializer.errors)
		return Response(errors, status=status.HTTP_400_BAD_REQUEST)
