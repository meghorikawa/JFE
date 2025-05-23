

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"on one hand", "on the other hand" 

お母さんは優しい一方で、お父さんはこわい。
父は自分に厳しい一方で、他人には優しい。
彼女の仕事は夏は非常に忙しい一方、冬は暇になる。
彼は俳優である一方で、歌手としても活躍している。
海外旅行は非日常を体験できることから、楽しいと感じることが多い一方で、不安なこともある。
その仕事はあまり面白くなかったが、その一方で給与はよかった。
老人の人口が増えている一方で、若年労働力の数がどんどん減っています。


'''
def match_ippou_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN", "lemma": {"IN":["一方", "いっぽう"]}},
        ],
        ]


    matcher.add("ippou", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
