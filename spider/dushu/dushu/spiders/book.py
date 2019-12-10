# -*- coding: utf-8 -*-
import scrapy
from dushu.items import DushuItem


class BookSpider(scrapy.Spider):
    name = 'book'
    # allowed_domains = ['xdushu.com']
    start_urls = ['https://www.x88dushu.com/xiaoshuo/111/111516/']

    def parse(self, response):
        if response.url == self.start_urls[0]:
            self.logger.info('访问小说目录'+response.url)
            li_list = response.css("div.mulu ul li a")
            for li in li_list:
                link = li.css('a::attr(href)').extract_first()
                yield scrapy.Request(self.start_urls[0]+link)
        else:
            self.logger.info('访问小说内容'+response.url)
            novel = response.css('div.novel')
            item = DushuItem()
            item['chapterName'] = novel.css('h1::text').extract_first()
            item['text'] = novel.css('div.yd_text2::text').extract()
            # self.logger().info(item)
            yield item
        # pass
