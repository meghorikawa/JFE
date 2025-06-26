

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

intend to; plan to do ~

Verb + つもり

今夜カラオケへ行くつもりだ。
今日はラーメンを食べるつもりだ。
あなたたちも行くつもりですか？


'''


def match_tsumori_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN", "lemma": "つもり"},
            {"lemma": {"NOT_IN":["で"]}}
          ],
    ]

    matcher.add("tsumori", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
