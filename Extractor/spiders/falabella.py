# -*- coding: utf-8 -*-
import json
import scrapy
import time
from urllib.parse import urlencode, quote_plus
import urllib
from Extractor.items import Productos



class TestingSpider(scrapy.Spider):
	name = 'falabella'
	api_url = 'http://www.falabella.com/rest/model/falabella/rest/browse/BrowseActor/get-product-record-list?'
	allowed_domains = ['falabella.com']
	start_urls = ['http://www.falabella.com']

	def parse(self, response):
		for menu_element in response.css('li.fb-masthead__grandchild-links__item'):
			up_cat = str(menu_element.css('a::text').extract_first()).strip()
			up_cat_url = str(menu_element.css('a::attr(href)').extract_first()).strip()
			if up_cat and 'VER TODO' not in up_cat.upper():
				up_cat_url = response.urljoin(up_cat_url)
				#navegando por los links
				request = scrapy.Request(url=up_cat_url, callback=self.getSubCategory)
				request.meta['up_cat'] = up_cat
				#request.meta['up_cat_url'] = up_cat_url
				yield request


	def getSubCategory(self,response):
		up_cat = response.meta['up_cat']
		up_cat_url = response.url #response.meta['up_cat_url']

		if response.css('div.fb-hero-subnav--nav__block'):
			for menu_element in response.css('div.fb-hero-subnav--nav__block'):
				h3 = menu_element.css('h3::text').extract_first()
				if h3 and 'VER TODO' not in str(h3).upper():
					for sub_menu_element in menu_element.css('li'):
						cat = str(sub_menu_element.css('a::text').extract_first()).strip()
						cat_url = str(sub_menu_element.css('a::attr(href)').extract_first()).strip()

						#Transformar el siguiente código a una funcion de tipo request
						nextPage = "1"
						curentUrl = cat_url
						nextUrl = '{"currentPage":' + nextPage + ',"navState":"' + curentUrl +  '"}'
						nextUrl = nextUrl.replace("http://www.falabella.com", "")
						nextUrl = nextUrl.replace("https://www.falabella.com", "")
						nextUrl = nextUrl.replace("www.falabella.com", "")
						nextUrl = nextUrl.replace("/falabella-cl", "")
						api_url = 'http://www.falabella.com/rest/model/falabella/rest/browse/BrowseActor/get-product-record-list?'
						nextUrl = api_url + str(urllib.parse.quote(nextUrl, safe='~()*!.\''))
						
						head_req = {'Content-Type': 'application/json'}

						request = scrapy.Request(url=nextUrl, callback=self.getProducts, method="GET", headers=head_req)

						request.meta['up_cat'] = up_cat
						request.meta['up_cat_url'] = up_cat_url
						request.meta['cat'] = cat
						request.meta['cat_url'] = response.urljoin(cat_url)

						yield request

				elif not h3:
					cat = str(menu_element.css('a::text').extract_first()).strip()
					cat_url = str(menu_element.css('a::attr(href)').extract_first()).strip()

					nextPage = "1"
					curentUrl = cat_url
					nextUrl = '{"currentPage":' + nextPage + ',"navState":"' + curentUrl +  '"}'
					nextUrl = nextUrl.replace("http://www.falabella.com", "")
					nextUrl = nextUrl.replace("https://www.falabella.com", "")
					nextUrl = nextUrl.replace("www.falabella.com", "")
					nextUrl = nextUrl.replace("/falabella-cl", "")
					api_url = 'http://www.falabella.com/rest/model/falabella/rest/browse/BrowseActor/get-product-record-list?'
					nextUrl = api_url + str(urllib.parse.quote(nextUrl, safe='~()*!.\''))
					
					head_req = {'Content-Type': 'application/json'}

					request = scrapy.Request(url=nextUrl, callback=self.getProducts, method="GET", headers=head_req)

					request.meta['up_cat'] = up_cat
					request.meta['up_cat_url'] = up_cat_url
					request.meta['cat'] = cat
					request.meta['cat_url'] = response.urljoin(cat_url)

					yield request
		else:
			nextPage = "1"
			curentUrl = response.url
			nextUrl = '{"currentPage":' + nextPage + ',"navState":"' + curentUrl +  '"}'
			nextUrl = nextUrl.replace("http://www.falabella.com", "")
			nextUrl = nextUrl.replace("https://www.falabella.com", "")
			nextUrl = nextUrl.replace("www.falabella.com", "")
			nextUrl = nextUrl.replace("/falabella-cl", "")
			api_url = 'http://www.falabella.com/rest/model/falabella/rest/browse/BrowseActor/get-product-record-list?'
			nextUrl = api_url + str(urllib.parse.quote(nextUrl, safe='~()*!.\''))
			
			head_req = {'Content-Type': 'application/json'}

			request = scrapy.Request(url=nextUrl, callback=self.getProducts, method="GET", headers=head_req)

			request.meta['up_cat'] = up_cat
			request.meta['up_cat_url'] = response.url
			request.meta['cat'] = up_cat
			request.meta['cat_url'] = response.url

			yield request
			
	def getProducts(self,response):
		
		data = json.loads(response.text)

		if data['success']:
			for product in data['state']['resultList']:
				item = Productos()
				item['url'] = 'https://falabella.com' + product['url']
				item['name'] = product['title']
				for price in product['prices']:
					if price['type'] and price['type'] == 3:
						item['bprice'] = ''.join(x for x in price['originalPrice'] if x.isdigit())
					elif price['type'] and price['type'] == 2:
						item['price'] = ''.join(x for x in price['originalPrice'] if x.isdigit())
					elif price['type'] and price['type'] == 1:
						item['cprice'] = ''.join(x for x in price['originalPrice'] if x.isdigit())
					else:
						pass
				'''
				if item['price'] and item['price'] > 0 and item['bprice'] and item['bprice'] > 0:
					item['internetDiscOverNormal'] = int(round((1-(item['bprice']/item['price']))*100,0))
				if item['price'] and item['price'] > 0 and item['cprice'] and item['cprice'] > 0:
					item['cardDiscOverNormal'] = int(round((1-(item['cprice']/item['price']))*100,0))
				if item['cprice'] and item['cprice'] > 0 and item['bprice'] and item['bprice'] > 0:
					item['cardDiscOverInternet'] = int(round((1-(item['cprice']/item['bprice']))*100,0))
				'''
				item['date'] = time.strftime("%d/%m/%Y")
				item['page'] = data['state']['curentPage']
				item['cat_url'] = response.meta['cat_url']
				item['up_category_url'] = response.meta['up_cat_url']
				item['category'] = response.meta['cat']
				item['up_category'] = response.meta['up_cat']
				

				yield item

			if int(data['state']['curentPage']) < int(data['state']['pagesTotal']):

				nextPage = str(int(data['state']['curentPage']) + 1)
				curentUrl = response.meta['cat_url']

				nextUrl = '{"currentPage":' + nextPage + ',"navState":"' + curentUrl +  '"}'
				nextUrl = nextUrl.replace("http://www.falabella.com", "")
				nextUrl = nextUrl.replace("https://www.falabella.com", "")
				nextUrl = nextUrl.replace("/falabella-cl", "")

				api_url = 'http://www.falabella.com/rest/model/falabella/rest/browse/BrowseActor/get-product-record-list?'
				nextUrl = api_url + str(urllib.parse.quote(nextUrl, safe='~()*!.\''))

				head_req = {'Content-Type': 'application/json'}

				if nextUrl is not None:
					request = scrapy.Request(url=nextUrl, callback=self.getProducts, method="GET", headers=head_req)

					request.meta['up_cat'] = response.meta['up_cat']
					request.meta['up_cat_url'] = response.meta['up_cat_url']
					request.meta['cat'] = response.meta['cat']
					request.meta['cat_url'] = response.meta['cat_url']
					yield request

	#def putRequest(self,api_url,cat_url,up_cat_url,cat,up_cat,next_page)