import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

決して	Verb (ない form)
Noun + ではない
な-adjective + ではない
い-adjective -い + くない

あなたのことは決して忘れません。
私は決して夢をあきらめない。
決してあなたは一人じゃありません。
社長には、決して失礼な言葉を言ってはいけません。
'''


def match_keshitenai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern to allow for infinite span between 決してand negative
            {"lemma": "決して", "pos": "ADV"},  # 決して
            {"OP": "{,9}"},  # Allow up to a span of 9 tokens between
            {"lemma": {"IN": ["ない", "ぬ"]}, "pos": "AUX"}  # Ends with "ない" or "ん(ません)"
        ]
    ]

    matcher.add("keshitenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
