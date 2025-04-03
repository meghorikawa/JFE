import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Noun + ほど　+	Verb (ない form)
Noun + ほど　+Adjective (ない form)


英語の文法は日本語ほど難しくありません。
彼女ほど優しい人はいない。
東京ほど家賃の高いところはない。
私ほどあなたのことを大切に思っている人はいないだよ。
彼ほど頭のいい人はいない。

'''


def match_hodonai_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verbs
            {"pos": {"IN":["NOUN", "PRON", "PROPN"]}},  #any noun or pronoun
            {"pos": {"IN": ["ADP", "PART"]}, "lemma": {"IN": ["ほど", "程"]}},  # allow for both hiragana and kanji
            {"OP": "{,13}", "OP": "?"},  # Allow up to a span of 9 tokens between
            {"lemma": {"IN": ["ない", "ぬ"]}, "pos": {"IN": ["AUX", "ADJ"]}}  # Ends with "ない" or "ん(ません)"
        ]
    ]

    matcher.add("hodonai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
