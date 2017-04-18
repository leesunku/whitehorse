# -*- coding:utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
path = os.getcwd()
    
def get_html(url):
    return requests.get(url).text

def parser(html):
    return BeautifulSoup(html,"html.parser")

def parser_chosun_news_url(parser_data):
    div = parser_data.find("div", {"id" : "list_area"})
    dls = div.find_all("dl", {"class": "list_item"})
    result = []
    for dl in dls:
        dt = dl.find("dt")
        a_href = dt.find("a")["href"]
        result.append(a_href)
    return result

def make_text_file(urls, page):
    newpath = path + "\\news\\" + page 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    index = 0
    for url in urls:
        f = open(path + "\\news\\" + page + "\\" + "news" + str(index) + ".txt", 'w')
        f.write(url)
        f.close()
        index += 1
def crawler_run(page):
    news_url = "http://news.chosun.com/svc/list_in/list.html?pn="
    #news_url = "http://news.joins.com/politics/nk/list/1"
    html = get_html(news_url + page)
    parser_data = parser(html)
    urls = parser_chosun_news_url(parser_data)
    make_text_file(urls, page)
def main():
    max_page = 255
    for i in range(1, max_page):
        crawler_run(str(i))
main()