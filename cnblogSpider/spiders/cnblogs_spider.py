#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/10/17 下午10:15
# @File : cnblogs_spider.py
# @Software : PyCharm
# @Email ： 909709223@qq.com
import scrapy
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
            try:
                url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
                title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
                time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
                content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
                print(url,title,time,content)
            except Exception as e:
                print(e)
