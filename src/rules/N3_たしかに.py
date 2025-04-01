import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3


確かに phrase

パソコンの電源の付け方さえ分かりません。そんなこと、子供でさえ知っている。
忙しすぎて、ご飯を食べる時間さえない。
のどが痛くて、水さえ飲めない。
'''


def match_tashikani_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [
            {"pos": "ADJ", "orth": {"IN": ["確か", "たしか"]}},
            {"pos":"AUX", "orth":"に"}
        ]
    ]

    matcher.add("tashikani", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
