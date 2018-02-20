# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Productos(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    up_category_url = scrapy.Field()
    up_category = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    img	= scrapy.Field()
    category = scrapy.Field()
    cat_url = scrapy.Field()
    price = scrapy.Field()
    bprice = scrapy.Field()
    cprice = scrapy.Field()
    date = scrapy.Field()
    page = scrapy.Field()
    internetDiscOverNormal = scrapy.Field()
    cardDiscOverNormal = scrapy.Field()
    cardDiscOverInternet = scrapy.Field()



