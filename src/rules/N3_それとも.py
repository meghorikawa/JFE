import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

"or", "or else" 

歩こうか, それとも車で行こうか？
コーヒーはホットにしますか？それともアイスにしますか？
地下鉄で行きますか。それともJRで行きますか。
飲み物はコーヒーにしますか？それとも紅茶にしますか？


'''


def match_soretomo_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "CCONJ", "lemma": "それ"},
            {"pos": "ADP", "lemma": "と"},
            {"pos": "ADP", "lemma": "も"},
            {},

        ],
    ]

    matcher.add("soretomo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
