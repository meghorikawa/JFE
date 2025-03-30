import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: あまりに
JLPT Level: N3
'''
def match_amarini_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[
        #Rule pattern あまりに + Adj
        {"orth": "あまり", "pos": "ADJ"},
        {"orth": "に", "pos":"AUX"},
        {"pos": "ADJ"}

    ]

    matcher.add("あまりに", [patterns])
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)