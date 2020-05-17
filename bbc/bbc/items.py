# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class BbcItem(Item):
    title=scrapy.Field()
    description = scrapy.Field()
    time=scrapy.Field()
    related_topics=scrapy.Field()
    Type=scrapy.Field()
    url=scrapy.Field()
    
 