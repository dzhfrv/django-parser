import time
import requests

from apps.stats.models import Stats

from collections import Counter

from bs4 import BeautifulSoup


def url_processing(link):
    print('Start parsing')
    page = requests.get(link.link).content
    soup = BeautifulSoup(page, 'html.parser')
    tags = [tag.name for tag in soup.findAll(True)]

    # postgres JSONField requires dict-formatted data
    data = dict(Counter(tags))
    Stats.objects.create(url=link, tags=data)

    link.status = 1 # processing
    link.save()

    time.sleep(10)
    print(f'Parsing has ended for {link.link}')

    link.status = 3 # processed
    link.save()
