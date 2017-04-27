import os
import json
import chosun_crawler
from pprint import pprint

# http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# JPype install
# pip install JPype
# pip install konlpy
# pip install numpy
from konlpy.tag import Twitter

pos_tagger = Twitter()


PATH = os.getcwd()
PAGE_LENGTH = 3
START_PAGE = 1
def read_json(file_path):
    return chosun_crawler.get_html_for_file(file_path)

def convert_json_to_object(json_data):
    return json.loads(json_data)

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

if __name__ == "__main__":   
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
#    print(len(document))
#    for doc in document:
#        print(doc)
    
    to_doc = tokenize(document[0])
    pprint(to_doc)