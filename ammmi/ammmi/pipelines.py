# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class AmmmiPipeline(object):
    def process_item(self, item, spider):
        # r = requests.get(item['download_url'])
        # path = '../resource/'
        # if 'resource' not in os.listdir('../'):
        #     os.mkdir(path)
        # dirs = os.listdir(path)
        # if item['title'] not in dirs:
        #     os.mkdir('../resource/'+item['title'])
        # with open(item['save_directory'], 'wb') as f:
        #     f.write(r.content)
        return item


class AmmmiImagesPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
            # raise DropItem("Item contains no images")
        # if item['title'] not in os.listdir(self.IMAGES_STORE):
            # os.mkdir(self.IMAGES_STORE + '/' + item['title'])
        # 更改文件名
        # os.rename(self.IMAGES_STORE + "/" + image_paths[0], self.IMAGES_STORE + "/" + item['title'] + '/' + item['picture_name'] + '.jpg')
        # 更改图片路径名
        # item['image_path'] = self.IMAGES_STORE + "/" + item['title'] + '/' + item['picture_name']
        # item['image_paths'] = image_paths
        return item
