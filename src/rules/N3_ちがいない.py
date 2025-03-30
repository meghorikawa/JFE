import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual form)	+ に違いない
Noun + に違いない
な-adjective + に違いない
い-adjective + に違いない

中国人は漢字をたくさん知っているから、きっと日本の漢字もすぐに覚えられるに違いない。
'''


def match_chigainai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for nouns and Adjectives
            {"pos": {"IN":["NOUN", "ADJ","VERB","AUX"]}}, #do I need this? It may be good for tracking the type of
            # expressions created by the learners....
            {"orth": "に", "pos" : "ADP"},
            {"orth": {"IN": ["ちがい", "違い"]}, "pos": "NOUN"},
            {"orth":"ない","pos" : "AUX"}
        ],
        [  # Pattern for causative verbs。
            {"pos": {"IN":["NOUN", "ADJ"]}},
            {"orth": "に", "pos" : "ADP"},
            {"orth": {"IN": ["ちがい", "違い"]}, "pos": "NOUN"},
            {"orth":"ない","pos" : "AUX"}
        ]
    ]

    matcher.add("chigainai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
