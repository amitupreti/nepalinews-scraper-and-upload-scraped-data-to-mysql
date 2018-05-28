#verrsion 1 is the latest it srapes data real time when used with watch on linux  and uploads it to mysql server
# -*- coding: utf-8 -*-

import scrapy
from scrapy import Selector
from scrapy import Request

import time



#defining connection to mysql server
hostname='yourmysqlhostname'
username='yourmysqlusername'
dbname='youmysql database name'
password='password'


#importing pymysql
import pymysql.cursors



#establishing connection to mysql server
connection = pymysql.connect(host=hostname,
                             user=username,
                             password=password,
                             db=dbname,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



class OnlinekhabrSpider(scrapy.Spider):
    name = "onlinekhabr"

    #make changes to link here
    allowed_domains = ["onlinekhabar.com/content/news"]
    #start_urls = ('https://onlinekhabar.com/content/news/',)

    def __init__(self,address):
        self.start_urls = [address]

    def parse(self, response):
        
        links=response.xpath('//*[@class="news_loop"]/h2/a/@href').extract()
        for link in links:
            print(link)
            yield Request(link,callback= self.parse_article,dont_filter=True)

        
        nextpageurl = response.xpath('//*[@class="next page-numbers"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(nextpageurl)        
        yield scrapy.Request(absolute_next_page_url,dont_filter=True)




    def parse_article(self,response):
        title = response.xpath('//h1[@class="inside_head"]/text()').extract()
        title1 = title[0]
        article = response.xpath('//div[@class="ok-single-content"]/p/text()').extract()
        article1 = ''.join(article)
       
        title=title1.encode("utf-8", "strict")
        article=article1.encode("utf-8", "strict")


        #uploading to mysql server
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `Articles` (`title`, `article`,`link`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (title, article,'onlinekhabar'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()



       
