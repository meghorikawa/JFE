import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (dictionary form)	と共に
Noun

私の人生は、ギターと共にある。
春が近づくと共に、少しずつ暖かくなってきた。
私は共に戦ってくれる人を探している。
ツイッターでは情報を発信すると共に、様々な人と意見交換をしている。

'''


def match_totomoni_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb and noun
            {"pos":{"IN":["VERB","NOUN", "PRON"]}},
            {"lemma": "する", "pos": "AUX", "OP": "?"},  # optional auxiliary to account for する
            {"orth": {"IN":["と","は"]},"pos": "ADP", "OP": "?"}, # optional particle と
            {"orth": {"IN":["とも", "共"]}, "pos": "NOUN"},
            {"orth": "に", "pos": "AUX", "OP": "?"}
        ]
    ]

    matcher.add("totomoni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
