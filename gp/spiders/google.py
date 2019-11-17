# -*- coding: utf-8 -*-
import scrapy

# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from html.parser import HTMLParser as SGMLParser
from scrapy import Request
from urllib.parse import urljoin

from gp.items import GpItem


class GoogleSpider(scrapy.Spider):
    # print("HELLO STARTING")
    name = 'google'
    allowed_domains = ['play.google.com']
    start_urls = ['https://play.google.com/store/apps/']

    '''
    rules = [
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details",)), callback='parse_app', follow=True),
    ]
    '''

    def parse(self, response):
        print("CALLING PARSE")
        selector = scrapy.Selector(response)

        # print(response.body)

        urls = selector.xpath('//a[@class="LkLjZd ScJHi U8Ww7d xjAeve nMZKrb  id-track-click "]/@href').extract()

        link_flag = 0

        links = []
        for link in urls:
            # print("LINK" + str(link))
            links.append(link)

        for each in urls:
            yield Request(url="http://play.google.com" + links[link_flag], callback=self.parse_next, dont_filter=True)
            print("http://play.google.com" + links[link_flag])
            link_flag += 1

    def parse_next(self, response):
        selector = scrapy.Selector(response)

        # print(response)
        # app_urls = selector.xpath('//div[@class="details"]/a[@class="title"]/@href').extract()

        app_urls = selector.xpath('//div[@class="Vpfmgd"]/div[@class="RZEgze"]/div[@class="vU6FJ p63iDd"]/'
                                  'a[@class="JC71ub"]/@href').extract()

        urls = []
        for url in app_urls:
            url = "http://play.google.com" + url
            print(url)
            urls.append(url)

        link_flag = 0
        for each in app_urls:
            yield Request(url=urls[link_flag], callback=self.parse_app, dont_filter=True)
            link_flag += 1

    def parse_app(self, response):
        item = GpItem()
        item['app_url'] = response.url
        item['app_name'] = response.xpath('//h1[@itemprop="name"]').xpath('text()').extract()
        item['app_icon'] = response.xpath('//img[@itemprop="image"]/@src')
        # item['app_developer'] = response.xpath('//')
        # print(response.text)
        yield item
