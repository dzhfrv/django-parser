import time

from apps.stats.models import Stats


def url_processing(link):
    print('Start parsing')
    link.status = 1 # processing
    link.save()

    time.sleep(10)
    print(f'Parsing has ended for {link.link}')

    link.status = 3 # processed
    link.save()
