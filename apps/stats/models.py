from django.contrib.postgres.fields import JSONField
from django.db import models
from apps.links.models import Link


class Stats(models.Model):
    url = models.ForeignKey(
        Link,
        on_delete=models.CASCADE,
        related_name='stats',
    )
    tags = JSONField('tags')

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

