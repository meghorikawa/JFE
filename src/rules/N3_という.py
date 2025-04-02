import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N3

Noun	と言う, という
Phrase と言います, といいます

これは何という花ですか？
猫みたいだという人もいる。
彼が外国に行くという話がある。
'''


def match_toiu_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [# general patter
            {"pos": {"IN": ["NOUN", "PRON", "AUX"]}, "OP": "?"}, #optional as sometimes a phrase precedes do I want
            # to extract each of the forms?
            {"pos":"ADP", "orth":"と"},
            {"pos": "VERB", "lemma": {"IN": ["言う", "いう"]}},
            {"orth":{"NOT_IN":["より"]}}
        ]
    ]

    matcher.add("toiu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
