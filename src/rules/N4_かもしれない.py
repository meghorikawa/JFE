import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb (casual form)	+かも かもしれない
Noun                 かもしれません
な-adjective
い-adjective

難しいかも。
そうかもしれない。
病気かもしれない。
午後から雨が降るかもしれない。
来週、台風が来るかもしれない。
途中で雨が降るかもしれないから、傘を持っていきましょう。

'''


def match_kamoshirenai_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for casual form
            {"lemma": "か", "pos": "ADP"},
            {"lemma": "も","pos": "ADP"},
            {"lemma": "しれる","pos": "VERB","OP": "?"},
            {"lemma": "ない", "pos": "AUX","OP": "?"},
        ], [# pattern for polite form
            {"lemma": "か", "pos": "ADP"},
            {"lemma": "も", "pos": "ADP"},
            {"lemma": "しれる", "pos": "VERB", "OP": "?"},
            {"lemma": "ます", "pos": "AUX", "OP": "?"},
            {"lemma": "ぬ", "pos": "AUX", "OP": "?"},

        ]
    ]

    matcher.add("kamoshirenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
