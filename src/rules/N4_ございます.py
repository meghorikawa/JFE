import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

あります changes to ございます
います changes to ございます


です ->	でございます
ではありません ->	でございません

ご質問はございますか。
お忘れ物はございませんか。
お時間がございますか？
電話は階段の横にございます。
お釣でございます。
初めまして、経理部の佐藤でございます。
この件に関しましては、ただいま確認中でございます。
私からは以上でございます。

'''


def match_gozaimasu_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern affirmative ございます
            {"pos":{"IN": ["ADP", "AUX"]}}, # allow capture of any ADP for analysis of contexts ございます is used.
            {"pos":"VERB", "lemma": "ござる"},
            {"orth": "ます", "pos": "AUX"},
        ], [ # general pattern negative ございません
            {"pos": {"IN": ["ADP", "AUX"]}},  # allow capture of any ADP for analysis of contexts ございます is used.
            {"pos": "VERB", "lemma": "ござる"},
            {"orth": "ませ", "pos": "AUX"},
            {"lemma": "ぬ", "pos": "AUX"},
        ],# [# pattern for plain form leaving it out for now as things are being double counted.
           # {"pos": {"IN": ["ADP", "AUX"]}},  # allow capture of any ADP for analysis of contexts ございます is used.
            #{"pos": "VERB", "lemma": "ござる"},
        #]
    ]

    matcher.add("gozaimasu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
