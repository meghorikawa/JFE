import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

its better to

___ + ほうがいい・方がいい・方が良い

行かないほうがいい。
疲れたら、早く寝たほうがいい。
暑い日には、水をたくさん飲んだ方がいい。
寝る前に、スマホを使わない方がいい。

'''


def match_hougaii_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "NOUN", "lemma": {"IN": ["ほう","方"]}},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "ADJ", "lemma": {"IN": ["いい","良い"]}},
          ],
    ]

    matcher.add("hougaii", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
