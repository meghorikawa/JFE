import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


Verb ます (stem form)	ながら（も）
Verb (て form) + い
Noun
な-adjective
い-adjective

狭いながらも、このマンションは大好きだ。
残念ながらも、今日のイベントに行けません。
うちは貧しいながらも、家族の仲がいいし、幸せだ。
アナちゃんは子どもながらも、いろんなことを知っている。
彼女はダイエットすると言っていながら、今日もアイスを食べている。

'''


def match_nagaramo_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "SCONJ", "orth": "ながら"},
           # {"orth": "も", "pos": "ADP", "OP": "?"}, when adding this it is double counting so figure this out.
        ]
    ]

    matcher.add("nagaramo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
