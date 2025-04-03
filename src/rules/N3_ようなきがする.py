import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual) + ような	+気がする
Noun + のような
な-adjective + な
い-adjective + ような


それが本当のような気がする。
分かるような気がする。
今日は、宝くじが当るような気がする。
この食べ物を毎日食べると、太るような気がする。
卒業したのはつい昨日のような気がする。
その答えは「no」のような気がした。

need to think about how to handle punctuation 「」

'''


def match_younakigasuru_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # NOUN pattern Noun + のような +気がする
            {"pos": {"IN": ["NOUN", "PRON", "PROPN"]}},
            {"pos": "ADP", "lemma": "の"},
            {"pos": {"IN": ["AUX", "NOUN"]}, "lemma": "よう"},
            {"pos": "AUX", "orth": "な"},
            {"pos": "NOUN", "orth": {"IN": ["気", "き"]}}, # allow for hiragana and kanji
            {"pos": "ADP", "orth": "が"},
            {"pos": "VERB", "orth": "する"}

        ], [# VERB pattern Verb (casual) + ような
            {"pos": {"IN": ["VERB", "AUX"]}},
            {"pos": {"IN": ["AUX", "NOUN"]}, "lemma": "よう"},
            {"pos": "AUX", "orth": "な"},
            {"pos": "NOUN", "orth": {"IN": ["気", "き"]}}, # allow for hiragana and kanji
            {"pos": "ADP", "orth": "が"},
            {"pos": "VERB", "orth": "する"}

        ], [ # adjective pattern
            {"pos": {"IN": ["ADJ"]}},
            {"pos": "AUX", "orth": "な"},
            {"pos": {"IN": ["AUX", "NOUN"]}, "lemma": "よう"},
            {"pos": "AUX", "orth": "な"},
            {"pos": "NOUN", "orth": {"IN": ["気", "き"]}},  # allow for hiragana and kanji
            {"pos": "ADP", "orth": "が"},
            {"pos": "VERB", "orth": "する"}


        ]
    ]

    matcher.add("younakigasuru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
