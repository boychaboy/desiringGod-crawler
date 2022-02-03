import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["https://www.desiringgod.org/articles/all?sort=oldest"]
    start_urls = ["http://https://www.desiringgod.org/articles/all?sort=oldest/"]

    def parse(self, response):
        for article in response.xpath(
            "/html/body/div[5]/main/div[2]/div/div/a/@href"
        ).extract():
            pass
        pass
