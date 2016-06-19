import scrapy
import pymongo

class DmozSpider(scrapy.Spider):
    name = "xiaomi"
    allowed_domains = ["xiaomi.org"]
    start_urls = [
        "http://app.mi.com"
    ]

    client = pymongo.MongoClient("localhost", 27017)
    db = client.Xiaomi
    pages = db.pages

    def parse(self, response):
        base_url = response.url
        links = response.xpath('//ul[@class="applist"]/li/h5')

        for link in links:
            doc = {}
            doc['url'] = base_url + link.xpath('a/@href').extract()[0]
            doc['content'] = link.xpath('a/text()').extract()
            self.pages.insert(doc)