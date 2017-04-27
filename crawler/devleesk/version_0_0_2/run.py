# -*- coding:utf-8 -*-
import requests
import os
import json
import chosun_crawler 
from bs4 import BeautifulSoup
#sort
from operator import itemgetter
from time import localtime, strftime

PATH = os.getcwd()
PAGE_LENGTH = 5
START_PAGE = 1
NEWS_URL = "http://news.chosun.com/svc/list_in/list.html?pn="

# write url file, html file
def create_url_and_html_file():
    for page in range(START_PAGE, START_PAGE + PAGE_LENGTH):
        html = chosun_crawler.get_html_for_url(NEWS_URL + str(page))
        parser_data = chosun_crawler.html_parser(html)
        urls = chosun_crawler.get_news_url(parser_data)
        idx = 0
        for url in urls:
            
            single_news_html = chosun_crawler.get_html_for_url(url)
            single_news_parser_data = chosun_crawler.html_parser(single_news_html)
            
            url_dir_path = PATH+ "/url/page_" + str(page) + "/" 
            url_file_name = "url_" + str(idx) + ".txt"
            chosun_crawler.write_file(url_dir_path, url_file_name, str(url))
            
            html_dir_path = PATH + "/html/page_" + str(page) + "/" 
            html_file_name = "html_" + str(idx) + ".txt"
            chosun_crawler.write_file(html_dir_path, html_file_name, str(single_news_parser_data))
            
            idx += 1

# read html
def read_html(page, idx):
    file_path = PATH + "/html/page_" + str(page) + "/html_" + str(idx) + ".txt" 
    return chosun_crawler.get_html_for_file(file_path)

def read_url(page, idx):
    file_path = PATH + "/url/page_" + str(page) + "/url_" + str(idx) + ".txt" 
    return chosun_crawler.get_html_for_file(file_path)

def generate_data(parser_data, url):
    map = {}
    map["url"] = url
    map["title"] = chosun_crawler.get_news_title(parser_data)
    map["content"] = chosun_crawler.get_news_content(parser_data)
    map["date"] = chosun_crawler.get_news_date(parser_data)
    map["date"] = chosun_crawler.get_news_date(parser_data)
    map["category"] = chosun_crawler.get_news_category(parser_data)
    map["author"] = chosun_crawler.get_news_author(parser_data)
#    map["reply_count"] = int(chosun_crawler.get_news_reply_count(parser_data))
    map["reply_count"] = chosun_crawler.get_news_reply_count(parser_data)
#    map["like_count"] = int(chosun_crawler.get_news_like_count(parser_data))
    map["like_count"] = chosun_crawler.get_news_like_count(parser_data)
#    map["rt_count"] = int(chosun_crawler.get_news_rt_count(parser_data))
    map["rt_count"] = chosun_crawler.get_news_rt_count(parser_data)
    map["img_url"] = chosun_crawler.get_news_img_url(parser_data)
    map["img_comment"] = chosun_crawler.get_news_img_comment(parser_data)
    return map 

def write_json(html_dir_path, html_file_name, results):
    chosun_crawler.write_file(html_dir_path, html_file_name, convert_object_to_json(results))

def read_json(file_path):
    return chosun_crawler.get_html_for_file(file_path)

def convert_object_to_json(object_data):
    return json.dumps(object_data)

def convert_json_to_object(json_data):
    return json.loads(json_data)

if __name__ == "__main__":   
#    create_url_and_html_file()
    results = []
    for page in range(START_PAGE, START_PAGE + PAGE_LENGTH):
        for idx in range(0, 10):
            html = read_html(page, idx)
            url = read_url(page, idx)
            parser_data = chosun_crawler.html_parser(html)
            results.append(generate_data(parser_data, url))
    
#    results.sort(key=itemgetter("reply_count"))
#    for result in results:
#        if result["reply_count"] != "0":
#            print(result["reply_count"])
    
    html_dir_path = PATH + "/json//" 
    html_file_name = str(START_PAGE) + "_" + str(PAGE_LENGTH) + ".json"
#    write_json(html_dir_path, html_file_name, results)
   
    json_data = read_json(html_dir_path+html_file_name)
    data_arr = convert_json_to_object(json_data)

    document = []
    for data in data_arr:
        text = ""
        for con in data["content"]:
            text = text + con
        document.append(text)
    print(len(document))
    for doc in document:
        print(doc)
