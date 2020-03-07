import logging
from collections import Counter

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from apps.stats.models import Stats

logger = logging.getLogger(__name__)


def parse_tags(url: str) -> dict:
    try:
        page = requests.get(url)
        if page.status_code != 200:
            logger.error(f'{url} is {page.status_code}')
            return None
    except RequestException as error:
        logger.error(error)
        return None
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        tags = [tag.name for tag in soup.findAll(True)]
        data = dict(Counter(tags))
        return data


def url_processing(link):
    link.change_status('processing')
    data = parse_tags(link.link)

    if data is None:
        link.change_status('error')
        return

    Stats.objects.create(url=link, tags=data)
    logger.info(f'Stat has saved for link: {link.pk}')
    link.change_status('processed')
