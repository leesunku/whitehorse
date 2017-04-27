# -*- coding:utf-8 -*-
import nltk
import re
from konlpy.corpus import kobill
from konlpy.tag import Twitter
from nltk.corpus.reader.ieer import documents
from pprint import pprint
document1 = """배우 남궁민(39)이 SBS TV 드라마 '조작'(극본 김현정, 연출 이정흠)에 출연 확정했다고 소속사 935엔터테인먼트가 20일 밝혔다.
'조작'은 사회 부조리를 파헤치는 기자들의 이야기를 그린다. 남궁민은 사고뭉치 기자 '한무영'을 맡는다. 기자였던 형이 비리를 고발하다 억울하게 죽는 모습을 본 후 복수를 위해 직접 기자가 된 인물이다.
소속사는 "전작 '김과장'이 많은 사랑을 받아 차기작을 결정하는 데 많은 고민이 있었다. '조작'은 '김과장' 때와 달리 남궁민의 진지하고 카리스마 넘치는 매력을 보여줄 드라마"라고 말했다.
한편 '조작'은 2015년 방송된 SBS 2부작 드라마 '너를 노린다'에서 호흡을 맞춘 이정흠 PD와 김현정 작가가 다시 한번 의기투합한 작품이다. 드라마는 '엽기적인 그녀' 후속으로 7월 방송 예정이다.
"""
document2 = """[스포츠조선닷컴 이지현 기자] tvN 금토드라마 '시카고 타자기' 제작진이 5, 6회 방송에 대한 힌트를 전해 관심을 모으고 있다.
스토리가 전개될수록 흥미를 더하고 있는 '시카고 타자기'는 앞서 지난 3, 4회에서 유령작가 유진오(고경표 분)의 존재를 발견하고, 이로 인해 혼란을 거듭해 가는 스타작가 한세주(유아인 분)의 모습이 그려졌다. 특히 시종일관 여유로움을 잃지 않는 유진오의 캐릭터가 흥미를 더했다. 유진오는 진짜 그의 이름이 아닌, 한세주의 집필실에 걸려 있던 극작가 '유진 오닐'의 초상화를 보고 급조한 이름이었고, 한세주가 그를 밧줄로 꽁꽁 묶어 두었지만 그는 손쉽게 탈출했다. 또한 그는 전설(임수정 분)을 따라다니며 먼 발치에서 아련하게 바라보는 모습으로 캐릭터에 대한 호기심을 더욱 끌어올렸다.
제작진은 "예민하고 까칠한 한세주가 여유로운 성격의 유진오와 부딪치며 만들어지는 호흡이 굉장히 재미있다. 유진오라는 매력적인 캐릭터의 등장은 전설에 대한 한세주의 감정을 본격적으로 시작하게 하는 기폭제 역할도 하게 될 것"이라고 밝혔다. 이어 "이번 주 '시카고 타자기' 5, 6회에서는 그간 제시됐던 복선들의 물꼬가 터질 예정이다. 시청자가 가장 궁금해 하는 두 가지가 해소되면서 스토리의 퍼즐 조각이 조금씩 맞춰질 것"이라고 전해 기대감을 높였다.
한편 tvN '시카고 타자기'는 슬럼프에 빠진 베스트셀러 작가 '한세주'와 그의 이름 뒤에 숨은 유령작가 '유진오', 한세주의 열혈 팬에서 안티 팬으로 돌변한 작가 덕후 '전설', 그리고 의문의 오래된 타자기와 얽힌 세 남녀의 미스터리한 앤티크 로맨스를 그린다. '킬미 힐미', '해를 품은 달'의 진수완 작가, '공항 가는 길' 김철규 감독을 비롯해 유아인, 임수정, 고경표 등 최고의 배우들이 모인 드라마로 뜨거운 관심을 얻고 있다. 21일(금) 저녁 8시 5회 방송.
"""
document3 = """[스포츠조선닷컴 정유나 기자] '발칙한 동거 빈방있음'의 집주인 피오가 '누나 전용 안전바'로 변신했다. 김신영-홍진영과 함께한 첫 동거에서 순둥 막둥이 '피요미'로 귀여움을 한 몸에 받았던 집주인 피오가 놀이기구 위 겁에 질린 누나들을 다독이며 자신의 무서움도 잊은 채 '누나 전용 안전바'로 변신하는 '기습 심쿵 남동생 스킬'을 보여준 것.
오는 21일 방송되는 MBC 스타 리얼 동거 버라이어티 '발칙한 동거 빈방있음'(연출 최윤정/ 이하 발칙한 동거)에서는 프로 반칙러이자 겁쟁이 3인방으로 등극한 현실 삼남매 케미 3인방 피오-김신영-홍진영의 좌충우돌 놀이공원 봄 나들이 2탄이 공개된다.
지난 방송에서 무서운 놀이기구 탑승을 피하기 위해 각종 반칙을 일삼으며 웃음을 자아냈던 피오-김신영-홍진영이 또 다시 놀이기구에 탑승한 모습이 포착돼 폭소를 유발하고
있는 가운데 누나들의 마음을 심쿵하게 만드는 피오의 모습이 시선을 강탈한다.
탑승 전부터 홍진영은 "언니 때문에 지금 이지경인 거 아니야!"라며 무서움을 참지 못하고 설움을 폭발 시켰고, 김신영은 잔뜩 겁에 질린 멍한 표정으로 놀이기구에 올랐다.
공개된 사진 속에는 가장 겁이 많은 홍진영과 함께 나란히 롤러코스터에 탑승한 피오가 "내가 잡고 있어! 괜찮아!"라며 잔뜩 고개를 숙인 홍진영을 다독이며, 아찔한 높이에 롤러코스터가 도착하자 홍진영 앞으로 자신의 팔을 내밀어 '누나 전용 안전바'를 자처한 모습이 담겨 있어 보는 이들을 셀레게 만든다.
또한 먹이를 먹는 기린의 모습에 깜짝 놀란 귀여운 피오의 모습과 함께 홀로 롤러코스터에 탄 큰 누나 김신영이 세차게 부는 바람을 온 얼굴로 받아내는 모습까지 공개돼 보는 이들을 폭소케 만들고 있다.
'심쿵 남동생 스킬'을 선보인 피오의 반전 매력과 언제나 흥과 에너지 넘치는 현실 삼남매 케미를 보여주고 있는 이들의 폭소 유발 현장이 담긴 놀이공원 봄 나들이 2탄은 오는 21일 방송되는 '발칙한 동거 빈방있음'을 통해 확인할 수 있다.
"""
def special_haracter_remove(text):
    return re.sub("[\[\]~!@#$%^&*()_+-=`'\":;<>?,./|]"," ", text)
    

document1 = special_haracter_remove(document1)
document2 = special_haracter_remove(document2)
document3 = special_haracter_remove(document3)

t = Twitter()
keys1 = t.morphs(document1)
keys2 = t.morphs(document2)
keys3 = t.morphs(document3)

def tokenize(doc):
    return ['/'.join(t) for t in t.pos(doc, norm=True, stem=True)]

#print(tokenize(document1))
#print(tokenize(document2))
#print(tokenize(document3))
documents = []
documents.append(tokenize(document1))
documents.append(tokenize(document2))
documents.append(tokenize(document3))
#for d in documents:
#    print(d)
tokens = [t for d in documents for t in d]
#print(tokens)
#print(len(tokens))
text = nltk.Text(tokens, name='NMSC')
print(text)
print(len(text.tokens))
print(len(set(text.tokens)))
#pprint(text.vocab().most_common(10))
train_docs  = text.vocab().most_common(10)


# plot - pip install matplotlib
#text.plot(20)
# 플롯 차트 글씨 깨짐
"""
plot 그리는 부분
from matplotlib import font_manager, rc
font_fname = 'C:\Windows\Fonts\H2GTRE.TTF'
font_name = font_manager.FontProperties(fname=font_fname).get_name()
rc('font', family=font_name)
text.plot(20)
"""

"""
print(len(keys1))
print(len(keys2))
print(len(keys3))
keys = []
keys.append(keys1)
keys.append(keys2)
keys.append(keys3)
key = list(set(sum(keys,[])))
print(len(key))
"""

"""
이부분은 긍부정 수치가 있어야 가능한 예제...
pprint(train_docs) # train_docs[0]
selected_words = [text.vocab().most_common(10)]

def term_exists(doc):
    return {'exists({})'.format(doc)}

train_xy = term_exists(text)
classifier = nltk.NaiveBayesClassifier.train(train_xy)
print(nltk.classify.accuracy(classifier,train_xy))

print(train_xy)

"""