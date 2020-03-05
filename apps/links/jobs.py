import time
import json
import requests

from apps.stats.models import Stats

from collections import Counter

from bs4 import BeautifulSoup


def url_processing(link):
    print('Start parsing')
    page = requests.get(link.link).content
    soup = BeautifulSoup(page, 'html.parser')
    tags = [tag.name for tag in soup.findAll(True)]
    data = Counter(tags)
    json_data = json.dumps(data)
    print(type(json_data))
    print(json_data)
    # Stats.objects.create(url=link, tags=json_data)

    link.status = 1 # processing
    link.save()

    time.sleep(10)
    print(f'Parsing has ended for {link.link}')

    link.status = 3 # processed
    link.save()
