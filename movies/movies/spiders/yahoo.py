import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['yahoo.com.tw']
    start_urls = ['http://yahoo.com.tw/']

    def parse(self, response):
        pass
