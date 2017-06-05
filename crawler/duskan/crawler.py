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

    def _init_projcess(self):
        pass

    def _crawling_data(self, url):
        pass
#bs = BeautifulSoup()

class ChosunURLCrawler(Crawler):
    def __init__(self):
        self.page_no = 1

    def _get_next_url(self):
        page_no = self.page_no
        url = "http://news.chosun.com/svc/list_in/list.html?pn={:d}".format(page_no)
        if page_no is 100:
            return ""
        self.page_no += 1
        return url

    def run(self):
        url_list = []
        while(True):
            url = self._get_next_url()
            print(url)
            if url == "":
                print("[system] : END URL")
                break
            html_context = requests.get(url).content
            bs = BeautifulSoup(html_context,"html.parser")
            current_url_list = []
            for dl in bs.find_all("dl"):
                current_url_list.append(dl.find("dt").find("a")["href"])
            if len(current_url_list) == 0:
                break
            url_list += current_url_list
        # write url in file
        url_file_name = "url_list.txt"
        f = open(url_file_name, 'w')
        for url in url_list:
            f.write(url+"\n")
        f.close()



if __name__ == "__main__":
#    url = "http://news.chosun.com/svc/list_in/list.html?pn=1"
#    html_context = requests.get(url).content
#    bs = BeautifulSoup(html_context,"html.parser")
#    url_list = []
#    for dl in bs.find_all("dl"):
#        url_list.append(dl.find("dt").find("a")["href"])
#    for url in url_list:
#        print(url)
    # get or update parsing url:
    cho_u_crl = ChosunURLCrawler()
    cho_u_crl.run()

