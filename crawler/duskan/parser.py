from data_component import ChosunData
from bs4 import BeautifulSoup


class Parser:
    pass


class ChosunParser(Parser):
    def __init__(self):
        pass

    def parse_data(self,url, html_data):
        bs = BeautifulSoup(html_data,"html.parser")
#        try:
        title = bs.find_all("h1",{"id":"news_title_text_id"})[0].text
        category_tag = bs.find_all("div",{'class':"news_title_cat"})[0].find("a")
        category = category_tag.text if category_tag else ""
        content = "\n".join([div.text for div in bs.find_all("div",{'class':"par"})])
        
        return ChosunData(
                url=url,
                title=title,
                category=category,
                content=content,
            )
#        except Exception as e:
#            print(str(e))
#            print("@@@@@@@@@@@@@@@@@@@@@@@@@")
#            return None



