

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

intend to; plan to do ~

Verbた + り + Verbた + り
Noun/なadj＋　だったり +Noun/なadj＋　だったり
いadj+かったり + いadj+かったり

休みの日は水曜日だったり、日曜日だったりです。
日曜日は買い物したり、映画を見たりした。
私の店は忙しかったり暇だったりです。

'''


def match_tari_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": {"IN":["PART","ADP"]}, "lemma": "たり"},
            {},
          ],
    ]

    matcher.add("tari", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
