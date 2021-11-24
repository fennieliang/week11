#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:11:31 2021

@author: fennieliang
"""

'''
in terminal under the same folder as the program type:
scrapy runspider week1105_scrapy.py -o quotes.txt
-o quotes.jl is to write a file named quotes.jl
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movies.yahoo.com.tw']
    start_urls = ['http://movies.yahoo.com.tw/']

    def parse(self, response):
        for quote in response.css('div.movielist_info'):
            #get everything between <div class="quote"...>...</div>
            
            yield{
                'name': quote.xpath('h2/a/text()').get(),
                #get each author between <span ...>...<small...>(...)</small>..</span>
                'date': quote.xpath('h3/text()').get(),
                #get each text between <span class="text"...>(...)
            }
        next_page = response.css('li.next a::attr("href")').get()
        #get next page
        if next_page is not None:
            yield response.follow(next_page, self.parse)