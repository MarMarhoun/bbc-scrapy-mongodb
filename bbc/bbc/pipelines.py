# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class BbcPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_port):
        self.mongo_uri=mongo_uri
        self.mongo_db = mongo_db
        self.mongo_port = mongo_port

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_port= crawler.settings.get('MONGODB_PORT')
            #mongo_collection=crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        # create a connection to mongodb
        self.client=pymongo.MongoClient(self.mongo_uri,self.mongo_port)
        # create the database "bbcDB"
        self.db=self.client[self.mongo_db]

    def process_item(self, item, spider):
        #name of the collection
        name = "News"
        # insert the data into a mongodb database
        self.db[name].insert(dict(item))
        return item

    
    def close_spider(self, spider):
        self.client.close()