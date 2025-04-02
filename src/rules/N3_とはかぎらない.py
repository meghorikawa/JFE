import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N3

Verb (casual)	+ とは限らない
Noun + だ
な-adjective + だ
い-adjective

先生の答えがいつも正しいとは限りません。
こういう音楽は誰でも好きだとは限らない。
お金持ちになれば、必ず幸せになるとは限りません。
いい大学を卒業したから、いい会社に入れるとは限らない。
無料のほうがいいとは限らない。無料のものは質が低いものが多いです。

'''


def match_tohakagiranai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # plain form
            {"pos": "ADP", "orth": "と"},
            {"pos": "ADP", "orth": "は"},
            {"pos": "VERB", "lemma": "限る"},
            {"pos": "AUX", "lemma": "ない"}
        ],[ # polite form
            {"pos": "ADP", "orth": "と"},
            {"pos": "ADP", "orth": "は"},
            {"pos": "VERB", "lemma": "限る"},
            {"pos": "AUX", "lemma": "ます"},
            {"pos": "AUX", "lemma": "ぬ"}
        ]
    ]

    matcher.add("tohakagiranai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
