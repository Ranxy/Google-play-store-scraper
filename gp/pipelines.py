# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy import Item


class GpPipeline(object):
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DBNAME', 'scrapy_db')
        db_post = spider.settings.get('MONGODB_DOCNAME', 'apkinfo')

        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]
        self.post = self.db[db_post]

    def close_spider(self, spider):
        self.db_client.close()

    def process_item(self, item, spider):
        postItem = dict(item)
        self.post.insert(postItem)
        return item

    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)
        self.db.books.insert(item)