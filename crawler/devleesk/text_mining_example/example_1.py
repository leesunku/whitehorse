# -*- coding:utf-8 -*-
# pip install numpy
# pip install scipy
# pip install -U gensim
# pip install nltk 
# pip install konlpy 
# pip install twython 
# 환경 변수 java_home 설정 해야함
# python 과 java 의 bit가 동일 해야 함
doc1 = """배우 남궁민(39)이 SBS TV 드라마 '조작'(극본 김현정, 연출 이정흠)에 출연 확정했다고 소속사 935엔터테인먼트가 20일 밝혔다.
'조작'은 사회 부조리를 파헤치는 기자들의 이야기를 그린다. 남궁민은 사고뭉치 기자 '한무영'을 맡는다. 기자였던 형이 비리를 고발하다 억울하게 죽는 모습을 본 후 복수를 위해 직접 기자가 된 인물이다.
소속사는 "전작 '김과장'이 많은 사랑을 받아 차기작을 결정하는 데 많은 고민이 있었다. '조작'은 '김과장' 때와 달리 남궁민의 진지하고 카리스마 넘치는 매력을 보여줄 드라마"라고 말했다.
한편 '조작'은 2015년 방송된 SBS 2부작 드라마 '너를 노린다'에서 호흡을 맞춘 이정흠 PD와 김현정 작가가 다시 한번 의기투합한 작품이다. 드라마는 '엽기적인 그녀' 후속으로 7월 방송 예정이다.
"""
 
from konlpy.corpus import kobill
from konlpy.tag import Twitter
t = Twitter()
tokens_doc = t.morphs(doc1)

import nltk
ko = nltk.Text(tokens_doc, name='뉴스')
#print(len(ko.tokens))
#print(len(set(ko.tokens)))
print(list(set(ko.tokens)))
keys = list(set(ko.tokens))
ko.vocab()
#ko.plot(50)
#print(ko.count(str('드라마')))
#print(len(tokens_doc))
count_arr = []
for to in tokens_doc:
    m = {}
    m[to] = str(ko.count(str(to)))
    count_arr.append(m)
count_arr = set(count_arr)
print(count_arr)
keys = count_arr.keys()
compare = (lambda x: x.keys)
count_arr.sort(key=compare,reverse=True)
for c in keys:
    print(c[c])
    
#    print(str(to) + " - " + str(ko.count(str(to))))


# 출처 : http://blog.naver.com/PostView.nhn?blogId=2feelus&logNo=220384206922&redirect=Dlog&widgetTypeCall=true