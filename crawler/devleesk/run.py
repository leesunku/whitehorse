# -*- coding:utf-8 -*-
import crawler;
import os
path = os.getcwd()

if __name__ == "__main__":
    page = 3
    idx = 3
    newpath = path + "\\news\\" + str(page) + "\\" + "news" + str(idx) + ".txt"
    url = crawler.get_news_url(newpath)
    news_html = crawler.get_html(url)
    crawler.make_text_real_file(news_html,page)
    
    print(news_html)
    parser_data = crawler.parser(news_html)
    
    title = crawler.parser_chosun_news_title(parser_data)
    print("title - " + title)
    date = crawler.parser_chosun_news_date(parser_data)
    print("data - " + date)
    contents = crawler.parser_chosun_news_content(parser_data)
    for content in contents:
        print("content - " + content)
