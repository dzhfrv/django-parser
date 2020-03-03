from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.links import serializers
from .models import Link


class LinkResource(viewsets.ViewSet):
    """
    Resource for working with posts
    Authentication is required
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """
        GET /links/
        :param request:
        :return: List of all links
        """
        queryset = Link.objects.all()
        serializer = serializers.CreatePostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /links/
        Save a new link
        :param request:
        :return: id of created link
        """
        serializer = serializers.CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        link = serializer.save(user=request.user)
        return Response({'id': link.id}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """
        GET /links/<pk>/
        Get info about selected link
        :param request:
        :param pk: link id
        :return: Detail post info
        """
        queryset = Link.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CreatePostSerializer(user)
        return Response(serializer.data)
