import requests

from apps.stats.models import Stats

from collections import Counter

from bs4 import BeautifulSoup


def url_processing(link):
    print('Start parsing')
    link.status = 1  # processing
    link.save()
    page = requests.get(link.link).content
    response = requests.get(link.link)
    print(response)
    if response.status_code == 200:

        soup = BeautifulSoup(page, 'html.parser')
        tags = [tag.name for tag in soup.findAll(True)]

        # postgres JSONField requires dict-formatted data
        data = dict(Counter(tags))
        Stats.objects.create(url=link, tags=data)
        print(f'Parsing has ended for {link.link}')

        link.status = 3 # processed
        link.save()
    else:
        link.status = 2  # error in processing
        link.save()
        raise ValueError(f'Response Status Code - {response.status_code}')
