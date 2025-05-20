

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

states something is not quite impossible but requires great effort

VERB ない + ことはない
NOUN/adjective + ないor じゃない +ことはない

走れば間に合わないことはないよ。急ごう！
嬉しくないことはないが、1位が良かった。
車を運転できないことはないんですが、ほとんどしません。
鶏肉は、食べないことはないですが、あまり好きではありません。
できないことはないですけど、少し時間をいただきたいです。
私も留学したことがありますから、あなたの苦労が分からないことはありません。
これは美味しくないことはないですけど、家の近くのラーメン店の方が安くて美味しいです。
私も留学したことがありますから、あなたの苦労が分からないことはありません。

'''


def match_naikotohanai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": {"IN": ["AUX", "VERB"]}},
            {"pos": {"IN": ["ADJ", "AUX"]}, "lemma": "ない"},
            {"pos": "NOUN", "orth":{"IN":["こと", "事"]}},
            {"pos": "ADP", "lemma": "は"},
            {"pos": {"IN": ["AUX","VERB"]}, "lemma": "ない"},

        ],[ #adj pattern
            {"pos": "ADJ"},
            {"pos": {"IN": ["ADJ", "AUX"]}, "lemma": "ない"},
            {"pos": "NOUN", "orth":{"IN":["こと", "事"]}},
            {"pos": "ADP", "lemma": "は"},
            {"pos": {"IN": ["AUX","VERB"]}, "lemma": "ない"},

            ]
        ]


    matcher.add("naikotohanai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
