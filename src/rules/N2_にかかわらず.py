

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"in spite of", "regardless of~"

NOUN にかかわらず（関わらず）

このバスは距離にかかわらず、どこまで行っても200円だ。
値段にかかわらず、新しいiPhoneが発売したら買うつもりだ。
明日の国際交流イベントに来る来ないにかかわらず、連絡してください。
お酒を飲む飲まないに関わらず、飲み会の参加費は3,000円です。
好き嫌いに関わらず、家族のためにこの仕事は必ずしなければならない。
テストの点数に関わらず、間違えたところは復習するようにしてください。

'''
def match_nikakawarazu_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "SCONJ", "lemma": "に"},
            {"pos": "SCONJ", "lemma": {"IN": ["関わる","かかわる"]}},
            {"pos": "SCONJ", "orth": "ず" },
        ],
        ]


    matcher.add("nikakawarazu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
