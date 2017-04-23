import requests
import os
from bs4 import BeautifulSoup

sector = "culture"
category = "art"
page = 1

def main() :
    url = "http://news.joins.com/"+sector+"/"+category+"/list/"+str(page)+"?filter=OnlyJoongang"
    html = requests.get(url).content
    lxml_data = BeautifulSoup(html, "lxml")
    title_raw = lxml_data.find_all("strong",
                                        {"class": "headline mg"})

    for content_raw in title_raw:
        news_link = "http://news.joins.com/" + content_raw.find('a')['href']
        news_title = content_raw.find('a').text

        print(news_title + " - "+ news_link)
