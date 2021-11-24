#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:19:01 2021

@author: fennieliang
"""
'''
in terminal under the same folder as the program type:
scrapy runspider week1102_scrapy.py -o quotes.jl
-o quotes.jl is to write a file named quotes.jl
'''
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        #'http://quotes.toscrape.com/tag/humor/',
         'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            #get everything between <div class="quote"...>...</div>
            yield {
                #output the following results
                
                'author': quote.xpath('span/small/text()').get(),
                #get each author between <span ...>...<small...>(...)</small>..</span>
                'text': quote.css('span.text::text').get(),
                #get each text between <span class="text"...>(...)</span>
                
            }

        next_page = response.css('li.next a::attr("href")').get()
        #get next page
        if next_page is not None:
            yield response.follow(next_page, self.parse)