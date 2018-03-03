# -*- coding: utf-8 -*-
encoding = "utf-8"
import scrapy
import time
from Extractor.items import Productos


class ParisSpider(scrapy.Spider):
	name = 'paris'
	allowed_domains = ['paris.cl']
	start_urls = ['https://www.paris.cl/tienda/es/paris']

	pageSize = 30

	def parse(self, response):
		for menu_element in response.css('li.menu-item'):
			#if 'SEARCHDISPLAY' not in menu_element.css('a::attr(href)').extract_first():
			cat_name = str(menu_element.css('a::text').extract_first()).strip()
			url = str(menu_element.css('a::attr(href)').extract_first()).strip()
			if cat_name and 'SEARCH' in url.upper():
				item = Productos()
				item['category'] = cat_name
				item['cat_url'] = url
				#navegando por los links
				request = scrapy.Request(url=url, callback=self.getProducts)
				request.meta['item'] = item
				yield request


	def getProducts(self,response):
		item = response.meta['item']

		for product in response.css('div[class*=boxProduct]'):
			available = str(product.css('div#tipos_de_entrega > div[id*=stock_msg]::text').extract_first()).strip()
			if 'SIN STOCK' not in available:
				url_product = str(product.css('p[class*=text] > a::attr(href)').extract_first()).strip()
				img_product = str(product.css('div[class*=item] > a[class*=pdp] > img::attr(data-src)').extract_first()).strip()
				name_product = str(product.css('p[class*=text] > a::text').extract_first()).strip()
				normal_price = str(product.css('p[class*=normal] > span::text').extract_first()).strip()
				#if "INTERNET" in str(product.css('div[class*=precio_internet]::text').extract_first()).strip().upper():
				best_price = str(product.css('p[class*=internet]::attr(data-internet-price)').extract_first()).strip()
				card_price = str(product.css('div[class*=itemPrice] > p[class*=price]::text').extract_first()).strip()
				#else:
				#	best_price = str(product.css('div[class*=offerPrice]::text').extract_first()).strip()
				#	card_price = ""

				normal_price = ''.join(x for x in normal_price if x.isdigit())
				best_price = ''.join(x for x in best_price if x.isdigit())
				card_price = ''.join(x for x in card_price if x.isdigit())

				item['url'] = url_product
				item['img'] =  img_product[:img_product.find('?')]
				item['name'] = name_product
				item['price'] = normal_price
				item['bprice'] = best_price
				item['cprice'] = card_price
				item['date'] = time.strftime("%d/%m/%Y")

				yield item

		#pagination
		if (response.xpath('//*[@id="WC_CatalogSearchResultDisplay_div_1"]/div[1]/div[1]/b/text()').extract()[0]):
			itemsTotal = int(response.xpath('//*[@id="WC_CatalogSearchResultDisplay_div_1"]/div[1]/div[1]/b/text()').extract()[0])
			pages = int(round((int(itemsTotal) / int(self.pageSize)) - 0.5))
			items = self.pageSize
			itemsRestantes = int(itemsTotal) % int(self.pageSize)
			for x in str(pages):
				items = items + 30
				pagination = item['cat_url'] + "?beginIndex=" + str(items)
				request = scrapy.Request(pagination, callback=self.getProducts)
				request.meta['item'] = item
				yield request

			if itemsRestantes > 0:
				pagination = item['cat_url'] + "?beginIndex=" + str(itemsTotal - itemsRestantes)
				request = scrapy.Request(pagination, callback=self.getProducts)
				request.meta['item'] = item
				yield request