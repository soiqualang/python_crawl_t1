# -*- coding: utf-8 -*-
import scrapy


class Xskt1Spider(scrapy.Spider):
    name = 'xskt1'
    allowed_domains = ['xskt.com.vn']
    start_urls = ['http://xskt.com.vn/']

    def parse(self, response):
        pass
