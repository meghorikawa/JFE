import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"in addition", "besides"  

その上、そのレストランは私たちのホテルからとても近い。
この靴の値段は高い、その上デザインも良くない。
今日は暑いです。その上湿度も高い。
この仕事は面白いし、その上給料がいいのです。

'''


def match_sonoue_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "DET", "lemma": "その"},
            {"pos": "NOUN", "lemma": {"IN": ["上", "うえ"]}},
        ],
    ]

    matcher.add("sonoue", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
