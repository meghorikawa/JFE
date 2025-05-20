

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"merely"; "there is only..."

NOUN + でしかない

これらの考えは推測でしかない。
この作業は時間の無駄でしかない。
夢は夢でしかない。
もし薬で治らなかったら、手術でしかない。

'''


def match_deshikanai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN"},
            {"pos": "AUX", "lemma": {"IN":["だ","で"]}},
            {"pos": "ADP", "lemma": "しか"},
            {"pos": "AUX", "lemma": "ない"}
        ],
        ]


    matcher.add("deshikanai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
