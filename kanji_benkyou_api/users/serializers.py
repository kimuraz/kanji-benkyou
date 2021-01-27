from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer, for profile only.
    """
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')
        read_only_fields = ['email', 'username']
