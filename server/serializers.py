from rest_framework import serializers
from server.models import Venue, UserProfile, Gang
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

	username  = serializers.Field(source = 'user.username')

	class Meta:
		model = UserProfile
		depth =2
		fields = ('id', 'user', 'username','latitude', 'longitude', 'tagsCreated', 'tagsDeleted', 'money', 'gang')


class GangSerializer(serializers.ModelSerializer):
	gangsters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Gang
		fields = ('id', 'name', 'color', 'gangsters')


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email')


	def restore_object(self, attrs, instance=None):
		user = super(UserSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

	def to_native(self, obj):
		ret = super(UserSerializer, self).to_native(obj)
		del ret['password']
		return ret


	def get_nested_field(self, model_field):
		ret = super(UserSerializer, self).to_native(obj)
		del ret['password']
		return ret


class VenueSerializer(serializers.ModelSerializer):

	gang = serializers.Field(source='user.profile.gang')

	class Meta:
		model = Venue
		fields = ('id', 'name', 'user', 'gang', 'latitude', 'longitude', 'latestEditTimestamp', 'category')
