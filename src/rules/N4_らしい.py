import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb (casual form)	+   らしい
Noun                    らしく
な-adjective            らしくない
い-adjective

雨らしい。
男らしい。
女らしい。
学生らしくもっと勉強しなさい。
今日は君らしくないな。
遅刻するなんて彼らしくない。

'''


def match_yori_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for より
            { },
            {"pos": "AUX", "lemma": "らしい"},
            {}
        ],
    ]

    matcher.add("yori", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
