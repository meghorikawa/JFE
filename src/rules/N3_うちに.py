import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual form)	+ おかげで
Noun + の + おかげで
な-adjective + おかげで
い-adjective + おかげで


'''

def match_uchini_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[
        [ # Pattern for Verb (casual form)	+ うちに
        {"pos" : "VERB"},
        {"pos": "SCONJ", "OP" : "?"},
        {"orth" : "ない", "OP": "?"},  #optional negative,
        {"orth": "うち","POS": "NOUN"},
        {"pos": "ADP", "orth": "に"}
    ],
    [ #Pattern for Noun + の + うちに
        {"pos": "NOUN"},
        {"orth": "の"},
        {"orth": "うち", "POS": "NOUN"},
        {"pos": "ADP", "orth": "に"}
    ],
    [# pattern for both i and na adjectives
        {"pos": "ADJ"},
        {"pos":"AUX", "OP": "?"}, # optional space for な
        {"orth": "うち", "POS": "NOUN"},
        {"pos": "ADP", "orth": "に"}
    ]

    ]


    matcher.add("uchini", patterns)
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)