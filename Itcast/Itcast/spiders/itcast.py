# -*- coding: utf-8 -*-
import scrapy
from Itcast.Itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    # 爬虫名称（必选）
    name = 'itcast'
    # 爬取域范围（可选）
    allowed_domains = ['http://www.itcast.cn']
    # 起始url列表（必选）
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # node_list = response.css('div.li_txt')
        node_list = response.xpath("//div[@class='li_txt']")
        for node in node_list:
            item = ItcastItem()
            # .extract()讲xpath对象转换为字符串
            # name = node.css('h3.text::text').extract_first()
            name = node.xpath("./h3/text()").extract()
            # title = node.css('h4.text::text').extract_first()
            title = node.xpath("./h4/text()").extract()
            # info = node.css('p.text::text').extract_first()
            info = node.xpath("./p/text()").extract()
            #
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # print(name[0])
            # print(title[0])
            # print(info[0])
            yield item

