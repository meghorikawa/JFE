import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: あまり〜ない
JLPT Level: N3
'''
def match_amari_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[[
        #Rule pattern あまり　＋V　＋neg
        {"orth": "あまり"},
        {"pos":"VERB"},
        {"orth": "ない"}
    ],
    [# Rule pattern あまり食べません。
        {"orth" : "あまり"},
        {"pos": "VERB"},
        {"orth": "ませ"},
        {"orth": "ん", "pos" : "AUX"}
    ],
    [ # Rule pattern あまりさむくない
        {"orth": "あまり"},
        {"pos": "ADJ"},
        {"orth": "ない"}
    ],
    [ # polite adj pattern あまりさむくありません
        {"orth": "あまり"},
        {"pos": "ADJ"},
        {"orth" : "ませ"},
        {"orth": "ん", "pos" : "AUX"}
    ],
    [ #long span あまり肉を食べない。
        {"orth": "あまり"},
        {"pos": "NOUN"},
        {"pos" : "ADP"},
        {'pos': 'VERB'},
        {'orth': 'ない'}
    ],
    [ #long span あまり肉を食べません。
        {"orth": "あまり"},
        {"pos": "NOUN"},
        {"pos" : "ADP"},
        {'pos': 'VERB'},
        {'orth': 'ませ'},
        {'orth': "ん"}
    ]

    ]

    matcher.add("あまり", patterns)
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)