from django.contrib.auth import get_user_model
from django.db import models


class Link(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='links',
    )
    link = models.CharField('link', max_length=200, blank=True)
    status = models.IntegerField('status')
    date_added = models.DateTimeField('date added', auto_now_add=True)

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
