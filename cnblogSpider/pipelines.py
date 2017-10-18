# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem


class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json','wb')

    def process_item(self, item, spider):
        # 对item的title进行判断，如果存在则存储，不存在则抛DropItem异常
        if item['title']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.decode("unicode_escape"))
            return item
        else:
            raise DropItem("Missing title in %s" % item)
