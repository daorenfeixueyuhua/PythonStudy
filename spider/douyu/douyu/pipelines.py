# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):

    # 图片的保存路径
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        print('====================================')
        # 获取图片连接
        image_url = item['imageLink']
        # 发送图片链接请求
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        # 更改文件名
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item['nickname'] + '.jpg')
        # 更改图片路径名
        item['imagePath'] = self.IMAGES_STORE + 'full/' + item["nickname"]
        return item

