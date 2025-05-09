

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

ご注文は以上ですか？
６歳以上の子どもはがっこうに通わなければならない。
私からは以上でございます。


'''


def match_ijyou_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN", "lemma": {"IN": ["いじょう", "以上"]}},

          ]
    ]

    matcher.add("ijyou", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
