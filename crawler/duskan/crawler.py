import requests
import os
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        pass

    def run(self):
        pass

    def _get_next_url(self):
        pass

    def _parse_data(self, text):
        pass


class ChosunCrawler:
    def __init__(self):
        pass

    def _init

    def _crawling_data(self, url):
        pass
#bs = BeautifulSoup()


if __name__ == "__main__":
    url = "http://news.chosun.com/svc/list_in/list.html?pn=1"
    html_context = requests.get(url).content
    bs = BeautifulSoup(html_context,"html.parser")
    url_list = []
    for dl in bs.find_all("dl"):
        url_list.append(dl.find("dt").find("a")["href"])
    for url in url_list:
        print(url)

