#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:58:56 2021

@author: fennieliang
"""

'''
for windows: conda install -c conda-forge scrapy
for mac: pip install scrapy


Scrapy is written in pure Python and depends on 
a few key Python packages (among others):

lxml, an efficient XML and HTML parser
parsel, an HTML/XML data extraction library 
written on top of lxml, w3lib, 
a multi-purpose helper for dealing 
with URLs and web page encodings
twisted, an asynchronous networking framework
cryptography and pyOpenSSL, 
to deal with various network-level security needs


start a new scrapy project:
1. from anaconda open terminal then cd 
    to a preferred directory then type:
        
    scrapy startproject xxx

2. view the newly created myProject type:
    ls 


3. type: 
    scrapy -h 
    
    to view all scrapy commands

The Global commands as listed below, 
which can be used at scrapy installed virtual environment
For example:


scrapy settings
scrapy runspider
scrapy shell 'xxxxx'
scrapy fetch
scrapy view
scrapy version


Project-only commands can only be used 
at the same folder as the python program:

.crawl
.check
.list
.edit
.parse
.bench



'''
#in terminal type the followings to see the results:
#scrapy shell 'http://quotes.toscrape.com/page/1/'
#response.css('title')
#response.css('title::text').getall()
#response.css('title').getall()
#response.css('title::text').get()
#response.css('title::text')[0].get()
#response.css('title::text').re(r'Quotes.*')
#response.css('title::text').re(r'Q\w+')
#response.css('title::text').re(r'(\w+) to (\w+)')
#response.xpath('//title')
#response.xpath('//title/text()').get()
#response.css("div.quote")

'''
for complete a scrapy program do the following 5 steps

1. scrapy startproject movies
2. cd movies
3. ls (check files in movies folder)
4. scrapy genspider movies movies.yahoo.com.tw
5. scrapy crawl movies -o movies.jl

please note for recording data not in English into files
the folloing line needs to be added to settings.py

FEED_EXPORT_ENCODING = 'utf-8'


'''
