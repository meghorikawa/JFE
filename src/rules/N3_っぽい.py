import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N3


Verb ます (stem form)	っぽい
Noun　+　っぽい
い-adjective -い + っぽい

油っぽい食事は好きじゃない。
私はあなたの子供っぽいところが好きです。
あの小学生は、大人っぽい。
年を取ると、忘れっぽくなる。

'''


def match_ppoi_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [
            {"pos": {"IN": ["NOUN", "VERB"]}},
            {"pos":"PART", "lemma":"っぽい"}
        ]
    ]

    matcher.add("ppoi", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
