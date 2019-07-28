# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liuhjhj
@File           :  html_downloader.py
"""
import urllib.request
import urllib.error


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
