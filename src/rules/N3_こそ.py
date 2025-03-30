import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: こそ
JLPT Level: N3

今日こそ早く寝るつもりだ。あなたこそ私の大切な友達です。努力こそ成功への鍵だ。今こそ行動を起こすべきだ。この本こそ探していたものだ。健康こそ何よりも大切だ。愛こそ人生の意味だと思う。あなたの努力こそ認められるべきだ。今度こそ試験に合格してみせる！親の気持ちこそ子供にはなかなか分からないものだ。
'''
def match_koso_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[
        {"orth": "こそ", "pos": "ADP"}
    ]


    matcher.add("こぞ", [patterns])
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)