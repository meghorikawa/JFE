import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Clause + つまり .....

彼は獣医、つまり、動物の医者です。
彼女は姉の娘だ。つまり、私にとっては姪です。
つまり、あなたは何も知らないのですね。

'''


def match_tsumari_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"orth": "つまり", "pos": "ADV"},
        ]
    ]

    matcher.add("tsumari", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
