# -*- coding:utf-8 -*-
import crawler;
import os
path = os.getcwd()

def main():
    page = 3
    idx = 3
    newpath = path + "\\news\\" + str(page) + "\\" + "news" + str(idx) + ".txt"
    url = crawler.get_news_url(newpath)
    news_html = crawler.get_html(url)
    parser_data = crawler.parser(news_html)
    
    title = crawler.parser_chosun_news_title(parser_data)
    print("title - " + title)
    contents = crawler.parser_chosun_news_content(parser_data)
    for content in contents:
        print("content - " + content)
main()