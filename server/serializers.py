from django.forms import widgets
from rest_framework import serializers
from server.models import User, Team, Venue

class UserSerializer(serializers.Serializer):

    pk = serializers.Field()
    nickname = serializers.CharField(max_length=100)


  def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.nickname = attrs.get('nickname', instance.nickname)
            return instance
        # Create new instance
        return Snippet(**attrs)
