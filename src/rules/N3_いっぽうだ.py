import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: V（dict）＋　一方だ。
JLPT Level: N3
環境破壊は年々進む一方だ。インターネットの普及により、オンラインサービスの需要が高まる一方です。
この国の人口は減少する一方だと報告されています。
感染症の拡大を防ぐためには、対策を強化する一方だろう。
'''
def match_ippouda_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[
        {"pos" : "VERB"},
        {"POS": "AUX", "OP": "?"}, # optional auxilary verb to accomodate for する constructions
        {"orth": "一方", "pos": "NOUN"},
        {"pos": "AUX"}
    ]


    matcher.add("一方だ", [patterns])
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)