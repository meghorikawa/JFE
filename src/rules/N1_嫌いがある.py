

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"bad Habbit" , "to have a tendency" 


VERB  + 嫌いがある
NOUNの

彼は物事を少しすぎる嫌いがある。
彼女は面接の時に緊張する嫌いがある。
この頃の若者は協調性に欠ける嫌いがある。
最近の子供はスマホやゲームの影響で夜遅くまで起きる嫌いがある。
うちの部長は自分と違う考え方を認めようとしない嫌いがある。
話をおもしろくするためだろうか、彼はものごとを大げさに言う嫌いがある。
彼は一度言い出したら、人の意見に耳を傾けない。少し独断の嫌いがある。



'''
def match_kiraigaaru_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": {"IN":["VERB","AUX"]}},
            {"pos":"NOUN","lemma": "嫌い"},
            {"pos":"ADP", "lemma": "が"},
            {"pos": {"IN":["AUX", "VERB"]}, "lemma": "ある"}
        ],[# pattern with NOUN
            {"pos": "NOUN"},
            {"pos":"ADP", "lemma": "の"},
            {"pos":"NOUN","lemma": "嫌い"},
            {"pos":"ADP", "lemma": "が"},
            {"pos": {"IN":["AUX", "VERB"]}, "lemma": "ある"}
        ]
        ]


    matcher.add("kiragaaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
