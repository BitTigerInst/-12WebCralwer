import scrapy
import re

from scrapy.selector import Selector
from appstore_crawler.items import AppstoreCrawlerItem


class XiaomiSpider(scrapy.Spider):
    name = "xiaomi"
    allowed_domains = ["app.mi.com"]

    start_urls = ["http://app.mi.com/category/5"]

    def parse(self, response):
        page = Selector(response)

        divs = page.xpath('//ul[@class="applist"]/li')

        for div in divs:
            item = AppstoreCrawlerItem()
            item['title'] = div.xpath('./h5/a/text()').extract()[0].encode('utf-8')
            item['url'] = div.xpath('./h5/a/@href').extract()[0]
            item['appid'] = re.match(r'/detail/(.*)', item['url']).group(1)
            item['intro'] = div.xpath('.//p[@class="app-desc"]/a/text()'). \
                extract()[0].encode('utf-8')
            yield item
