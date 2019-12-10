import scrapy
from ammmi.items import AmmmiItem

class AmmiSipder(scrapy.Spider):
    # spider name
    name = 'ammmi'
    # 表示允许爬虫爬的网站
    allowed_domains = ['www.ammmi.com']

    count = 0
    page_num = 1
    web_name = 'ammmi'
    base_url = 'https://www.ammmi.com/category/dongmantupian'
    start_urls = ['https://www.ammmi.com/category/dongmantupian']

    def parse(self, response):

        img_list = response.xpath('//a[@class="NavLinks"]/@href').extract()

        if len(img_list):
            for img in img_list:
                item = AmmmiItem()
                item['title'] = response.xpath('//h2[@class="titletips"]/text()').extract_first()
                item['picture_name'] = img[58:-4]
                item['image_url'] = img
                self.count += 1
                # if self.count >= 50:
                #     return
                yield item

        page_list = response.xpath('//div[@class="mi_cont "]//ul/li/h3/a/@href').extract()

        if len(page_list) == 0:
            return
        else:
            for page in page_list:
                yield scrapy.Request(page, callback=self.parse)

        if self.page_num >= 30:
            return

        self.page_num += 1

        yield scrapy.Request(self.base_url + '/page/' + str(self.page_num), callback=self.parse)
