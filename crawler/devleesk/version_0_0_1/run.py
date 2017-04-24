# -*- coding:utf-8 -*-
import requests
import os
import chosun_crawler
from bs4 import BeautifulSoup


path = os.getcwd()
#max_page = 5
page_length = 5
start_page = 1
news_url = "http://news.chosun.com/svc/list_in/list.html?pn="
# write url file, html file
def create_url_and_html_file():
    for page in range(start_page, start_page + page_length):
        html = chosun_crawler.get_html_for_url(news_url + str(page))
        parser_data = chosun_crawler.html_parser(html)
        urls = chosun_crawler.get_news_url(parser_data)
        idx = 0
        for url in urls:
            
            single_news_html = chosun_crawler.get_html_for_url(url)
            single_news_parser_data = chosun_crawler.html_parser(single_news_html)
            print(single_news_parser_data)
            
            url_dir_path = path + "/url/page_" + str(page) + "/" 
            url_file_name = "url" + str(idx) + ".txt"
            chosun_crawler.write_file(url_dir_path, url_file_name, str(url))
            
            html_dir_path = path + "/html/page_" + str(page) + "/" 
            html_file_name = "html_" + str(idx) + ".txt"
            chosun_crawler.write_file(html_dir_path, html_file_name, str(single_news_parser_data))
            
            idx += 1

# read html
def read_html():
    read_idx = 1;
    file_path = path + "/html/page_" + str(start_page) + "/html_" + str(read_idx) + ".txt" 
    return chosun_crawler.get_html_for_file(file_path)
if __name__ == "__main__":            
    #create_url_and_html_file()
    html = read_html()
    parser_data = chosun_crawler.html_parser(html)
    # code...
    title = chosun_crawler.get_news_title(parser_data)
    print(title)
    # code...
