# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liuhjhj
@File           :  spider_main.py
"""
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # URL下载器
        self.parser = html_parser.HtmlParser()  # URL解析器
        self.outputer = html_outputer.HtmlOutputer()  # URL输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count += 1
            except Exception as e:
                print('craw failed',e)

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
