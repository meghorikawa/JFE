import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (た form)	+ ところ
Verb (た form)	+ ばかり

今起きたところです。
昼ごはんを食べたところです。
アメリカから日本に戻ったところです。
駅に着いた時、ちょうど電車が出たところでした。
あなたのことを話したところだよ。
図書館にあなたを探しに行ったところです。
私は今起きたばかりです。
ずいぶん長くかかったのね。心配になっていたところよ。
この仕事を始めたばかりです。
田中さんは先月にこの会社に入ったばかりです。


also add ている +　ところ form

彼は入院しているところです。
今料理をしているところです。
私は今、家で日本語を勉強しているところです。
姉は電話をかけているところだ。
子どもを産んだばかりなので、うちで休んでいるところです。
彼女はお茶を飲みながら雑誌を読んでいるところです。

'''


def match_tokoro_bakari_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for てところ
            {"pos": "VERB"},
            {"pos": "AUX", "orth": "た"},
            {"pos": {"IN": ["NOUN","SCONJ"]}, "lemma": "ところ"},
        ],[# pattern for ばかり
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "た"},
            {"pos": "PART", "orth": "ばかり"},
        ], [# pattern for ているところ
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "する", "OP": "?"},
            {"pos": "SCONJ", "lemma" : {"IN" :["で", "て"]}},
            {"pos": "VERB", "lemma": "いる"},
            {"pos": {"IN": ["NOUN", "SCONJ"]}, "lemma": "ところ"},
        ]
    ]

    matcher.add("kashira", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
