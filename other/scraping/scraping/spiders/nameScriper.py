# -*- coding: utf-8 -*-
# does not work - scraper needs html/xml, not javascript
# scrapyJS migh be way around but page lists only first 20 fields, we need to select option all to see all
import scrapy
from scrapy import Selector

class NameIDSpider(scrapy.Spider):
    name = "nameSpider"
    start_urls = ['http://apps.ecmwf.int/codes/grib/param-db']

    def parse(self, response):
        print ('------------------')
        print ('------------------')
        print ('not working because this page uses javascript and to do scraping we need pure data(html/xml)')
        print ('------------------')
        print ('------------------')
        hxs = Selector(response)	
        rows = hxs.xpath('//tr')
        print(rows)
        for row in rows:
            print (row.xpath('td/text()').extract())
            print ("loop")
        pass

