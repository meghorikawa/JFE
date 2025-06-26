

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

the most; the best

NOUN + が・は　+ いちばん
いちばん + Phrase


彼がいちばん働いた。
午前中が一番調子がいい。
一番前に座っている人は誰ですか？
兄弟で誰が一番背が高いですか。

'''


def match_ichiban_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "ADV", "lemma": {"IN": ["いちばん", "一番"]}},
            {},
          ],
    ]

    matcher.add("ichiban", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
