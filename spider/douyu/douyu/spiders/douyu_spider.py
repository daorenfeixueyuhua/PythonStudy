import scrapy
from douyu.items import DouyuItem
import json


class DouyuSpider(scrapy.Spider):
    # spider name
    name = 'douyu'
    # 表示允许爬虫爬的网站
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.text)['data']
        if len(data_list) == 0:
            return
        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['imageLink'] = data['vertical_src']
            yield

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
