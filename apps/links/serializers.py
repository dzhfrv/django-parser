from rest_framework import serializers

from .models import Link

HUMAN_DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S %Z'


class CreateLinkSerializer(serializers.ModelSerializer):
    """
    Serializer for saving a Link
    Required fields: user, link
    """

    date_added = serializers.DateTimeField(
        format=HUMAN_DATETIME_FORMAT, read_only=True,
    )

    class Meta:
        model = Link
        exclude = ('user',)
