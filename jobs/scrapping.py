from random import choice
import requests
from bs4 import BeautifulSoup as BS


headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]

jobs = []

def habr_parsing():
    url = "https://habr.com/ru/all"
    res = requests.get(url, headers=choice(headers))
    if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        ul = soup.find('div', class_='tm-articles-list')
        li = ul.find_all('a', class_="tm-article-snippet__title-link")
        for i in li:
            url = 'https://habr.com' + i['href']
            res = requests.get(url,headers=choice(headers))
            title = i.text
            if res.status_code == 200:
                soup = BS(res.content, 'html.parser')
                divs = soup.find_all ('article',
                class_='tm-article-presenter__content tm-article-presenter__content_narrow')
                ratings = soup.find_all ('div', 
                class_='tm-company-card tm-company-article__company-card')
                infos = soup.find_all ('div', 
                class_="tm-company-basic-info")
                suits = soup.find_all ('ul', 
                class_='tm-widget-links__list')
                
                for div in divs:
                    user = div.find('a', class_='tm-user-info__username').text
                    hub = div.find('div', class_='tm-article-snippet__hubs').text
                    body = div.find('div', id='post-content-body').text
                    time = div.find('span', class_='tm-article-snippet__datetime-published').text
                    tag = div.find('ul', class_='tm-separated-list__list').text      
                
                for rating in ratings:
                    rate = rating.find('div', class_='tm-rating tm-company-card__rating').text

                for inf  in infos:  
                    suit = inf.find('a', class_='tm-company-basic-info__link').text
                    date = inf.find('dd', 
                    class_='tm-description-list__body tm-description-list__body_variant-columns-nowrap').text

            jobs.append({'url': url, 'title': title,
                        'tag': tag, 'body': body,'user': user, 
                        'time': time, 'ratings': rate,
                        'hub': hub,'suit': suit, 'date': date
                                        })

    return jobs
