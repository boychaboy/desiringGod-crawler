import requests
from time import time
import scrapy


CONTENT = "messages"  # ['articles', 'messages']


class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        start_time = time()
        article_urls = []
        offsets = range(0, 320)  # articles exists from 0 ~ 320 pages
        for offset in offsets:
            page_url = (
                f"https://www.desiringgod.org/{CONTENT}/all?page={offset}&sort=oldest"
            )
            yield scrapy.Request(page_url, self.parse)

    def parse(self, response):
        articles = response.xpath(
            "/html/body/div[5]/main/div[2]/div/div/a/@href"
        ).extract()
        urls = ["https://www.desiringgod.org" + article for article in articles]
        yield from response.follow_all(urls, self.parse_article)

    def parse_article(self, response):
        yield {
            "title": response.xpath("/html/body/div[5]/main/div[2]/header/h1/text()")
            .get()
            .strip(),
            "time": response.xpath("/html/body/div[5]/main/div[2]/header/time/text()")
            .get()
            .strip(),
            "body": " ".join(
                response.xpath("/html/body/div[5]/main/div[2]/div/p/text()").extract()
            ),
            "url": response.url,
        }
