from rest_framework import serializers
from server.models import Venue, UserProfile, Gang
from django.contrib.auth.models import User


class VenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venue
		fields = ('id', 'name', 'user', 'latitude', 'longitude', 'latestEditTimestamp', 'category')

class UserProfileSerializer(serializers.ModelSerializer):

	username = serializers.Field(source = 'user.username')

	class Meta:
		model = UserProfile
		fields = ('id', 'user', 'username','latitude', 'longitude', 'tagsCreated', 'tagsDeleted', 'money', 'gang')


class GangSerializer(serializers.ModelSerializer):
	gangsters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Gang
		fields = ('id', 'name', 'gangsters')


class UserSerializer(serializers.ModelSerializer):

	gang = serializers.ModelField(model_field=UserProfile()._meta.get_field('gang'))

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email', 'gang')


	def restore_object(self, attrs, instance=None):
		user = super(UserSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

	def to_native(self, obj):
		ret = super(UserSerializer, self).to_native(obj)
		del ret['password']
		return ret
