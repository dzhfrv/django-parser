from django.contrib.auth import get_user_model
from django.db import models

STATUSES = [
    (0, 'not processing'),
    (1, 'processing'),
    (2, 'error in processing'),
    (3, 'processed')
]


class Link(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='links',
    )
    link = models.URLField('link', max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)
    date_added = models.DateTimeField('date added', auto_now_add=True)

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
