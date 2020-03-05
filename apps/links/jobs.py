import time
import requests

from collections import Counter

from bs4 import BeautifulSoup


def url_processing(link):
    print('Start parsing')
    page = requests.get(link.link).content
    # print('PAGE', page)
    soup = BeautifulSoup(page, 'html.parser')
    tags = [tag.name for tag in soup.findAll(True)]
    data = Counter(tags)
    print(data)
    # soup.prettify()
    # document = soup.html.find_all()

    link.status = 1 # processing
    link.save()

    time.sleep(10)
    print(f'Parsing has ended for {link.link}')

    link.status = 3 # processed
    link.save()
