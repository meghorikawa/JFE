import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb ます (stem form)+ 気味
Noun + 気味 


'''

def match_gimi_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Verb (stem) + ぎみ
            {"pos": "VERB"},
            {"orth": {"IN": ["ぎみ", "気味"]}, "pos": "NOUN"}
        ],
        [  # Pattern for Noun + ぎみ
            {"pos": "NOUN"},
            {"orth": {"IN": ["ぎみ", "気味"]}, "pos": "NOUN"}
        ]
    ]

    matcher.add("gimi", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)