# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class NetianPipeline(ImagesPipeline):
    # 图片的保存路径
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        img_url = item['url']
        # print('开始获取: ' + img_url)
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        # print('路径：' + image_path[0])
        if not os.path.isdir(self.IMAGES_STORE + "/" + item['title']):
            os.mkdir(self.IMAGES_STORE + '/' + item['title'])


        os.rename(self.IMAGES_STORE + "/" + image_path[0],
                  self.IMAGES_STORE + "/" + item['title'] + "/" + item['name'] + '.jpg')
        return item
