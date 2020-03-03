from rest_framework import generics

from .serializers import UserRegistrationSerializer


class RegistrationEndpoint(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
