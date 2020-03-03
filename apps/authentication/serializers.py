from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    Required fields: 'email', 'password', 'first_name', 'last_name'
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
