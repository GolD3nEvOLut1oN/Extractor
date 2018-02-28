# -*- coding: utf-8 -*-
import scrapy
import time
from Extractor.items import Productos


class RipleySpider(scrapy.Spider):
	name = 'ripley'
	allowed_domains = ['simple.ripley.cl']
	start_urls = ['http://simple.ripley.cl/']

	def parse(self, response):
		for menu_element in response.css('li.child-category'):
			cat_name = str(menu_element.css('a::text').extract_first()).strip()
			url = str(menu_element.css('a::attr(href)').extract_first()).strip()
			if cat_name and cat_name.upper() != 'NONE' and 'VER TODO' not in cat_name.upper() and 'VER TODAS' not in cat_name.upper():
				item = Productos()
				item['category'] = cat_name
				item['cat_url'] = response.urljoin(url)
				#navegando por los links
				url = response.urljoin(url)
				request = scrapy.Request(url=url, callback=self.getProducts)
				request.meta['item'] = item
				yield request


	def getProducts(self,response):
		item = response.meta['item']

		for product in response.css('.catalog-product'):
			if (not product.css('.catalog-product-unavailable-text')):
				url_product = str(product.css('.catalog-product::attr(href)').extract_first()).strip()
				img_product = str(product.css('img::attr(data-src)').extract_first()).strip()
				name_product = str(product.css('.catalog-product-name::text').extract_first()).strip()
				normal_price = str(product.css('span.catalog-product-list-price::text').extract_first()).strip()
				best_price = str(product.css('span.catalog-product-offer-price::text').extract_first()).strip()
				card_price = str(product.css('span.catalog-product-card-price::text').extract_first()).strip()

				normal_price = ''.join(x for x in normal_price if x.isdigit())
				best_price = ''.join(x for x in best_price if x.isdigit())
				card_price = ''.join(x for x in card_price if x.isdigit())

				item['url'] = 'https://simple.ripley.cl' + url_product
				#item['img'] = 'https:' + img_product
				item['name'] = name_product
				item['price'] = normal_price
				item['bprice'] = best_price
				item['cprice'] = card_price
				#item['date'] = time.strftime("%d/%m/%Y")

				yield item
			else:
				pass

		next_page_url = response.xpath('//ul[@class="pagination"]//li[position() = (last())]/a/@href').extract_first()
		if next_page_url is not None:
			next_page_url = response.urljoin(next_page_url)
			request = scrapy.Request(url=next_page_url, callback=self.getProducts)
			request.meta['item'] = item
			yield request

