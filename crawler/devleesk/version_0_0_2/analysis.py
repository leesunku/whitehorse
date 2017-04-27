# -*- coding:utf-8 -*-
import nltk
import re
import os
import json
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from nltk.corpus.reader.ieer import documents
from pprint import pprint
import chosun_crawler

t = Twitter()
PATH = os.getcwd()
PAGE_LENGTH = 5
START_PAGE = 1

def write_json(html_dir_path, html_file_name, results):
    chosun_crawler.write_file(html_dir_path, html_file_name, convert_object_to_json(results))

def read_json(file_path):
    return chosun_crawler.get_html_for_file(file_path)

def convert_json_to_object(json_data):
    return json.loads(json_data)

def convert_object_to_json(object_data):
    return json.dumps(object_data)

def special_haracter_remove(text):
    return re.sub("[\[\]~!@#$%^&*()_+-=`'\":;<>?,./▲■‘’“”…|]"," ", text)

def tokenize(doc):
    return ['/'.join(t) for t in t.pos(doc, norm=True, stem=True)]

if __name__ == "__main__":   
    html_dir_path = PATH + "/json//" 
    html_file_name = str(START_PAGE) + "_" + str(PAGE_LENGTH) + ".json"
    
    json_data = read_json(html_dir_path+html_file_name)
    data_arr = convert_json_to_object(json_data)

    for data in data_arr:
        text = ""
        for con in data["content"]:
            text = text + con
        data["special_haracter_remove_data"] = special_haracter_remove(text)
        data["tokenize_data"] = tokenize(data["special_haracter_remove_data"])
        data["tokens"] = nltk.Text(data["tokenize_data"], name='NMSC').vocab().most_common(5)
#    for doc in data_arr:
#        print(doc["tokens"])
        
    analysis_dir_path = PATH + "/analysis//" 
    analysis_file_name = str(START_PAGE) + "_" + str(PAGE_LENGTH) + ".json"
    
    #write_json(analysis_dir_path, analysis_file_name, data_arr)
    
    json_data = read_json(analysis_dir_path+analysis_file_name)
    analysis_data_arr = convert_json_to_object(json_data)
    #print(analysis_data_arr)