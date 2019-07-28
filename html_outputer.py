# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liuhjhj
@File           :  html_outputer.py
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        count = 1
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<meta charset='UTF-8'>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%d</td>" % count)
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            count += 1

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
