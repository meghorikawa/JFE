import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

VERB  + 次第
"as soon as", "dependent upon"

Noun　+ 次第で、次第だ
"depending on"

我々が成功できるかどうかは君次第だ。
花火大会は天気次第で中止になる場合もあります。
結婚した相手次第で人生が決まってしまうこともある。
部屋の準備ができ次第、会議を始めます。
雨がやみ次第、出発することにしましょう。
詳しいことは情報が入り次第、お伝えします。
式が終了次第、ロビーに集合してください。

'''


def match_shidai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "NOUN", "lemma": {"IN":["次第","しだい"]}},
            {},
        ],
    ]

    matcher.add("shidai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
