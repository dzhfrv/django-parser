import logging

from django.contrib.auth import get_user_model
from django.db import models

logger = logging.getLogger(__name__)

STATUSES = [
    (0, 'not processing'),
    (1, 'processing'),
    (2, 'error in processing'),
    (3, 'processed'),
]
STATUS_MAPPER = {
    'not_processing': 0,
    'processing': 1,
    'error': 2,
    'processed': 3,
}


class Link(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='links',
    )
    link = models.URLField('link', max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)
    date_added = models.DateTimeField('date added', auto_now_add=True)

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

    def change_status(self, status):
        if status not in STATUS_MAPPER:
            return
        self.status = STATUS_MAPPER[status]
        self.save()
        logger.info(f'Link {self.pk} status has changed to {self.status}')
