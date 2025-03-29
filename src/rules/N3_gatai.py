import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Grammar Form Matched: こそ
JLPT Level: N3
'''
def match_gatai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)


    patterns =[
        {"orth": "こそ", "pos": "ADP"}
    ]


    matcher.add("こぞ", patterns)
    matches = matcher(doc)

    #from here I should figure out how I want to normalize the counts...
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)