import celery
from scrapy.crawler import CrawlerProcess

from surf_scrapers.spiders.waves import WavesSpider


@celery.task(name='hello')
def hello():
    return print('hello world')


@celery.task(name='waves-crawler')
def crawl_waves():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(WavesSpider)
    process.start()