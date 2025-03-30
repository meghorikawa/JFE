import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual form)	+ おかげで　とてもいい医者にみてもらったおかげで病気が治りました。
Noun + の + おかげで　　今日、皆さんのおかげで私の夢を実現しました。
な-adjective + な + おがげで　　綺麗なお陰で、掃除が楽でした。
い-adjective + おかげで　　せまいおかげで、あまり人呼べない。

とてもいい医者にみてもらったおかげで病気が治りました。

'''

def match_okagede_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Verb (casual form) + おかげで
            {"pos": "VERB"},
            {"pos": "AUX", "OP": "?"},  # Optional auxiliary (negative/past)
            {"orth": {"IN": ["おかげ", "お陰"]}, "pos": "NOUN"},
            {"orth": "で", "pos": "ADP"}
        ],
        [  # Pattern for Noun + の + おかげで
            {"pos": "NOUN"},
            {"orth": "の", "pos": "ADP"},  # の (particle)
            {"orth": {"IN": ["おかげ", "お陰"]}, "pos": "NOUN"},
            {"orth": "で", "pos": "ADP"}
        ],
        [  # Pattern for i-adjective + おかげで OR na-adjective + な + おかげで
            {"pos": "ADJ"},
            {"orth": "な", "pos": "AUX", "OP": "?"},  # Optional な for な-adjectives
            {"orth": {"IN": ["おかげ", "お陰"]}, "pos": "NOUN"},
            {"orth": "で"}
        ]
    ]

    matcher.add("okagede", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)