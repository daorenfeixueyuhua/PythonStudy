# -*- coding: utf-8 -*-
import scrapy

from netian.items import NetianItem


class NetianspiderSpider(scrapy.Spider):
    name = 'netianSpider'
    # allowed_domains = ['http://pic.netbian.com']
    start_urls = ['http://pic.netbian.com/']

    offset = 1

    spidered_urls = []

    def parse(self, response):
        # self.logger.info('start+++++++++++')
        # http://pic.netbian.com/
        # 获取图片的url：response.xpath('//ul[@class="clearfix"]/li').extract()

        img_list = response.xpath('//ul[@class="clearfix"]/li//a//@href').extract()

        if len(img_list) != 0:
            for url in img_list:
                yield scrapy.Request(self.start_urls[0] + url, callback=self.parse)

                # 开始爬取图片：response.xpath('//div[@class="photo-pic"]//img').extract()
        img_url = response.xpath('//div[@class="photo"]//div[@class="photo-pic"]//img').extract()
        # print(img_url)
        if img_url:
            item = NetianItem()
            item['url'] = self.start_urls[0] + response.xpath('//div[@class="photo-pic"]//img//@src').extract()[0]
            print(item['url'])
            if item['url'] not in self.spidered_urls:
                item['title'] = response.xpath('//div[@class="loaction"]//a//text()')[1].extract()
                item['name'] = response.xpath('//div[@class="photo-pic"]//img//@title').extract()[0]
                # self.logger.info('准备开始爬取' + item['url'])
                self.spidered_urls.append(item['url'])
                yield item

        # 访问下一页
        max_page = 1100
        if self.offset > max_page:
            return
        self.offset += 1
        self.logger.info('开始访问第' + str(self.offset) + '页')
        yield scrapy.Request(self.start_urls[0] + '/index_' + str(self.offset) + '.html', callback=self.parse)
