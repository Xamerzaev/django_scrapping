import django
from django.db import DatabaseError
from bs4 import BeautifulSoup as BS

import os
import sys

import requests
from random import choice

from jobs.models import Xamerz

headers = [
    {'User-Agent':
     'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
     'Accept':
     'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent':
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/49.0.2623.112 Safari/537.36',
     'Accept':
     'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent':
     'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
     'Accept':
     'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]

proj = os.path.dirname(os.path.abspath('manage.py'))

sys.path.append(proj)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

django.setup()


def habr_parsing():
    jobs = []
    url = "https://habr.com/ru/all"
    res = requests.get(url, headers=choice(headers))

    if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        ul = soup.find('div', class_='tm-articles-list')
        li = ul.find_all('a', class_="tm-article-snippet__title-link")
        for i in li:
            url = 'https://habr.com' + i['href']
            res = requests.get(url, headers=choice(headers))
            title = i.text
            if res.status_code == 200:
                soup = BS(res.content, 'html.parser')
                divs = soup.find_all('article', class_='\
                                     tm-article-presenter__content\
                                     tm-article-presenter__content_narrow')
                ratings = soup.find_all('div', class_='tm-rating__counter')
                infos = soup.find_all('section', class_="\
                                     tm-block tm-block_spacing-bottom")
                for div in divs:
                    try:
                        user = div.find('a', class_='\
                            tm-user-info__username').text
                        hub = div.find('div', class_='\
                            tm-article-snippet__hubs').text
                        body = div.find('div', id='post-content-body').text
                        time = div.find('span', class_='\
                            tm-article-snippet__datetime-published').text
                        tag = div.find('ul', class_='\
                            tm-separated-list__list').text
                        date = div.find('span', class_="\
                            tm-article-snippet__datetime-published").text

                    except Exception:
                        user = 'не найдено'
                        hub = 'не найдено'
                        body = 'не найдено'
                        time = 'не найдено'
                        tag = 'не найдено'

                for rating in ratings:
                    try:
                        rate = rating.find('div', class_='\
                            tm-rating__counter').text
                    except Exception:
                        rate = 0

                for inf in infos:
                    try:
                        suit = inf.find('a', class_='\
                            tm-company-basic-info__link').text
                        date = inf.find('span', class_="\
                            tm-article-snippet__datetime-published").text
                    except Exception:
                        suit = 'не найдено'
                        date = 'не найдено'

            jobs.append({
                'url': url, 'title': title,
                'tag': tag, 'body': body, 'user': user,
                'time': time, 'rate': rate,
                'hub': hub, 'suit': suit, 'date': date
                })

    return jobs


def save_posts():
    habr_news = habr_parsing()
    for i in habr_news:
        j = Xamerz(**i)
        try:
            j.save()
        except DatabaseError:
            pass


if __name__ == '__main__':
    habr_parsing()
    save_posts()
