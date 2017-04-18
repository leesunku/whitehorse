# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

page_num = 1
url = "http://news.chosun.com/svc/list_in/list.html?pn=1"
#url = "http://news.joins.com/politics/nk/list/1"
    
def get_html(url):
    return requests.get(url).text
def parser(html):
##    return BeautifulSoup(html,'lxml')
    return BeautifulSoup(html,"html.parser")
def main():
    html = get_html(url)
    parser_data = parser(html)
    dl = parser_data.find("dl", {"class": "list_item"})
    dt = dl.find("dt")
    a = dt.find("a")["href"]
    print(a)
main()