import requests
import os
import click
from bs4 import BeautifulSoup

from parser import ChosunParser


class Crawler:
    def __init__(self):
        pass

    def run(self):
        pass

    def _get_next_url(self):
        pass

    def _parse_data(self, text):
        pass


class ChosunCrawler(Crawler):
    def __init__(self):
        self.url_handler = URLHandler()
        self.parser = ChosunParser()
        self.data_list = []

    def run(self):
        while True:
            url = self._get_next_url()
            if url == "":
                break
            data_component = self._crawling_data(url)
            if data_component == None:
                continue
            self.data_list.append(data_component)
            
    def save_as_file(self, path=""):
        for data in self.data_list:
            self._save_data_as_file(data, path=path)
    
    def _save_data_as_file(self, data, path=""):
        file_name = path + "{}.txt".format(data.contents['id'])
        content = data.export_to_str()
        f = open(file_name, 'w')
        f.write(content+"\n")
        f.close()

    def _get_next_url(self):
        return self.url_handler.get_next_url()

    def _crawling_data(self, url):
        html_data = ""
        parser = self.parser 
        html_data = requests.get(url).content
        data_component = parser.parse_data(url, html_data)
        return data_component


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


class URLHandler:
    def __init__(self):
        self.url_file_path = "url_list.txt"
        self.index = 0
        self.url_list = []
        self.load_url()
        
    def load_url(self):
        url_file_path = self.url_file_path
        f = open(url_file_path, 'r')
        url_list = f.readlines()
        self.url_list = url_list

    def get_next_url(self):
        index = self.index
        url_list = self.url_list
        if len(url_list) <= index:
            return ""
        print("{:d}/{:d} {}".format(index, len(self.url_list), url_list[index].strip()))
        self.index += 1
        return url_list[index].strip()


@click.group()
def update_url():
    pass

@update_url.command()
def get_url():
    cho_u_crl = ChosunURLCrawler()
    cho_u_crl.run()

@update_url.command()
def parse_data():
    crawler = ChosunCrawler()
    crawler.run()
    print("run finished ")
    print("start saving result")
    crawler.save_as_file()

if __name__ == "__main__":
    update_url.add_command(get_url)
    update_url.add_command(parse_data)
    update_url()
