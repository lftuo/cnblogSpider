#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/17 下午10:15
# @File : cnblogs_spider.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
import scrapy
import sys

from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from cnblogSpider.items import CnblogspiderItem

reload(sys)
sys.setdefaultencoding('utf-8')

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"  # 爬虫的名称
    allowed_domins = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/qiyeboy/default.html?page=1"
    ]

    def parse(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath(".//*[@class='day']")
        # 从每篇文章中抽取数据

        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            # print url,title,time,content
            item = CnblogspiderItem(url=url,title=title,time=time,content=content)
            #request = scrapy.Request(url=url,callback=self.parse_body())
            #request.meta['item'] = item # 将item暂存
            yield item
        # 翻页功能
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0],callback=self.parse)

    def parse_body(self,response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['image_urls'] = body.xpath('.//img/@src').extract() # 提取图片链接

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('cnblogs')
    process.start()
