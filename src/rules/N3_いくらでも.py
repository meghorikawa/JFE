import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: いくら〜でも
JLPT Level: N3
examples:
いくら勉強しても、テストの点が上がらない。
いくら頼んでも、彼は手伝ってくれない。
いくら仕事が大変でも、夢を諦めたくない。
いくら納豆を食べても、好きにならない。
いくら好きでも、そんなことはできない。
'''
def match_amari_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[[# Rule pattern いくら　＋V　ても。。。
        {"orth": "いくら", "pos": "ADV"},
        {"POS": "NOUN", "OP": "?"},
        {"POS": "ADP", "OP": "?"},
        {"pos":"VERB"},
        {"POS": "AUX", "OP": "?"},
        {"orth": {"IN": ["て", "で"]}, "pos": "SCONJ"},
        {"orth":"も", "pos": "ADP"},
    ],
    [  # Rule pattern いくら　＋N + が+ADJ +でも。。。
        {"orth": "いくら", "pos": "ADV"},
        {"POS": {"IN" : ["NOUN", "PRON"]}, "OP": "?"},     # optional noun
        {"POS": "ADP", "OP": "?"},         # Optional particle
        {"pos":"ADJ"},
        {"orth": "で"},
        {"orth": "も", "pos": "ADP"},
    ]

    ]

    matcher.add("いくらでも", patterns)
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)