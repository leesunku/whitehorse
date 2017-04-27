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
    with open(dir_path + file_name, "w", encoding='utf8') as f:
        f.write(data)

def read_file(path):
    f = open(path, "r", encoding='utf8')
    return f.read()

def html_parser(html):
    return BeautifulSoup(html,"lxml")

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
    try:
        content_divs = div.find_all("div", {"class": "par"})
        result = []
        for content_div in content_divs:
            content_text = content_div.text
            result.append(content_text)
        return result
    except AttributeError as e:
#        print("get_news_content - " + str(content_text))
        return ""


def get_news_date(parser_data):
    p = parser_data.find("p", {"id" : "date_text"})
    return p.text

def get_news_category(parser_data):
    try:
        div = parser_data.find("div", {"class" : "news_title_cat"})
        a = div.find("a")
        return a.text
    except AttributeError as e:
#        print("get_news_category - " + str(a))
        return ""

def get_news_author(parser_data):
    try:
        li = parser_data.find("li", {"id" : "j1"})
        a = li.find("a")
        return a.text
    except AttributeError as e:
#        print("get_news_author - " + str(a))
        return ""

def get_news_reply_count(parser_data):
    try:
        span = parser_data.find("span", {"id" : "BBSCNT"})
        return span.text
    except AttributeError as e:
#        print("get_news_reply_count - " + str(div))
        return ""
def get_news_like_count(parser_data):
    try:
        span = parser_data.find("span", {"id" : "FBCNT"})
        return span.text
    except AttributeError as e:
#        print("get_news_like_count - " + str(div))
        return ""

def get_news_rt_count(parser_data):
    try:
        span = parser_data.find("span", {"id" : "TWCNT"})
        return span.text
    except AttributeError as e:
#        print("get_news_rt_count - " + str(div))
        return ""

def get_news_img_url(parser_data):
    
    try:
        div = parser_data.find("div", {"class" : "news_imgbox"})
        figure = div.find("figure")
        img_src = figure.find("img")["src"]
        return img_src
    except AttributeError as e:
#        print("get_news_img_url - " + str(div))
        return ""

def get_news_img_comment(parser_data):
    try:
        div = parser_data.find("div", {"class" : "news_imgbox"})
        figure = div.find("figure")
        return figure.find("figcaption").text
    except AttributeError as e:
#        print("get_news_img_comment - " + str(div))
        return ""
