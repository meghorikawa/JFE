import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


Noun	（で）さえ（も）

パソコンの電源の付け方さえ分かりません。そんなこと、子供でさえ知っている。
忙しすぎて、ご飯を食べる時間さえない。
のどが痛くて、水さえ飲めない。
'''


def match_sae_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern to allow for infinite span between 決してand negative
            {"pos": "NOUN"},
            {"pos":"ADP", "orth":"で", "OP": "?"},
            {"orth": "さえ", "pos": "ADP"}
        ]
    ]

    matcher.add("sae", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
