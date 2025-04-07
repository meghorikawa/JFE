import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4




Verb (て form)	いただけませんか

写真を取っていただけませんか。
ちょっと待っていただけませんか。
もう少しゆっくり話していただけませんか。
いい先生を紹介していただけませんか？
荷物を持ってきていただけませんか？

'''


def match_teitadakimasen_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["VERB", "AUX"]}},
            {"pos": "SCONJ", "lemma": "て"},
            {"pos": "VERB", "lemma":  "いただける"},
            {"pos": "AUX", "lemma": "ます"},
            {"pos": "AUX", "lemma": "ぬ"}
        ]
    ]

    matcher.add("teitadakimasen", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
