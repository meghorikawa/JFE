import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

Verb (casual)	恐れがある,おそれがある
Noun + の



梅雨に入ってからほとんど雨が降っていない。このまま降らないと、水不足になる恐れがある。
大きい地震が来たら、この建物は倒れる恐れがある。
この番組は子供に悪い影響を与える恐れがある。
台風がこのまま北上すると、日本に上陸する恐れがある。
こんなに赤字が続くと、この会社は倒産の恐れがある。

'''


def match_osoregaru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "NOUN", "lemma": {"IN": ["おそれ","恐れ"]}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "VERB", "lemma": "ある"},
          ],
    ]

    matcher.add("osoregaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
