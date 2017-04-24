# -*- coding:utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
path = os.getcwd()

def get_html_for_url(url):
    return requests.get(url).content

def get_html_for_file(path):
    return read_file(path)

def write_file(dir_path, file_name, data):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    try:
        with open(dir_path + file_name, "w") as f:
            f.write(data)
    except UnicodeEncodeError as e:
        with open(dir_path + file_name, "w", encoding='utf8') as f:
            f.write(data)
        print(e)

def read_file(path):
    f = open(path, "r")
    return f.read()

def html_parser(html):
    return BeautifulSoup(html,"html.parser")
#    return BeautifulSoup(html, from_encoding="utf-8")

def get_news_url(parser_data):
    div = parser_data.find("div", {"id" : "list_area"})
    dls = div.find_all("dl", {"class": "list_item"})
    urls = []
    for dl in dls:
        dt = dl.find("dt")
        a_href = dt.find("a")["href"]
        urls.append(a_href)
    return urls

def get_news_title(parser_data):
    h1 = parser_data.find("h1", {"id" : "news_title_text_id"})
    return h1.text

def get_news_content(parser_data):
    div = parser_data.find("div", {"id" : "news_body_id"})
    content_divs = div.find_all("div", {"class": "par"})
    result = []
    for content_div in content_divs:
        content_text = content_div.text
        result.append(content_text)
    return result


