# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_name = scrapy.Field()
    app_url = scrapy.Field()
    app_icon = scrapy.Field()
    app_developer = scrapy.Field()
    app_rate = scrapy.Field()
    app_version = scrapy.Field()
    app_description = scrapy.Field()
