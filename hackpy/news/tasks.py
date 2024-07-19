from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import News

@shared_task
def crawl_hackernews():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.select('.athing'):
        title = item.select_one('.titleline a').get_text()
        url = item.select_one('.titleline a')['href']
        news, created = News.objects.get_or_create(title=title, defaults={'url': url})
        if not created:
            news.url = url
            news.save()
