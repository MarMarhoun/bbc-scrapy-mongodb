



import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bbc.loaders import *
from scrapy import Request
from bbc.items import BbcItem





class BbcSpider(CrawlSpider):
    name = "bbc"
    start_urls = ['https://www.bbc.com/']

    rules=(Rule(LinkExtractor(allow='bbc.com', restrict_xpaths='//div[contains(@class,"module__content")]'
                                                               '//div[contains(@class,"media") and not (contains(@class,"media--icon"))]'
                                                               '//a[contains(@class,"block-link__overlay-link")]'
                              , process_value=lambda x: 'https://www.bbc.com' + x if x[0:1] == "/" else x),
                callback='parse_item'),
           )
    #This function is used to parse the infomation of the articles on bbc home page
    def parse_item(self, response):
        if response.status==200:
            item=BbcItem()
            #use xpath to extract the wanted infomation
            item['title']=response.xpath('//div[@class="story-body"]//h1/text()').extract_first()
            item['description']=response.xpath('//p[@class="story-body__introduction"]/text()').extract_first()
            item['url']= response.url
            item['Type']=response.xpath('//div[contains(@class,"secondary-navigation")]//a[contains(@class,"secondary-navigation__title")]/span/text()').extract_first()
            if item['Type'] is None:
                item['Type'] = response.xpath("//div[@class='container-width-only']//span[@class='index-title__container']//a/text()").extract_first()
                #two ways to get Type
            item['time']=response.xpath('//div[@class="story-body"]//ul[@class="mini-info-list"]//div/text()').extract_first()
            item['related_topics']= response.xpath('//div[@id="topic-tags"]//li/a/text()').extract_first()
            if item['time'] is not None:
                yield item