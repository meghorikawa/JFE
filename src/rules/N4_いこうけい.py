import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N4

Volitional in Japanese

今日から自転車で出勤しよう。
もう11時だ。早く寝よう。
重たそうだね。手伝おうか。
今日は食堂で昼食を食べよう。
図書館で一緒に勉強しよう。
明日は週末ですから、飲みに行こう。
雨が降っているよ。駅まで送ってあげようか？

this is a bit difficult as the ようform is not parsed seperately.... think on this for a bit...

'''


def match_ikoukei_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [# する　→　しよう　
            {"pos":"VERB"},
            {"pos": "AUX", "lemma": "しよう"}
        ],[ # 五段　ーれる
            {"pos": "VERB"},
            {"pos": "AUX","lemma": "ます"},
            {"pos": "AUX", "lemma": "しよう"}
        ]
    ]

    matcher.add("ikoukei", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
