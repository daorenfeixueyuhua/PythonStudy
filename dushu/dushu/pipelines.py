# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DushuPipeline(object):

    def process_item(self, item, spider):
        file = open('mulu/' + item['chapterName'] + '.txt', 'w', encoding='utf-8')
        for text in item['text']:
            file.write(text + '\n')
        file.close()
        return item

