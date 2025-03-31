import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb + たびに
Nounの + たびに

この曲を聞くたびに、家族を思い出す。
友人は旅行のたびにお土産を買ってきてくれます。
あの人を会うたびに用事を頼まれる。
ミスをするたびに部長にしかられる。
買い物のたびに、袋をたくさんもらう。

'''


def match_tabini_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb
            {"pos": "VERB"},
            {"pos": "NOUN", "orth": "たび"},
            {"orth": "に", "pos": "ADP"}
        ], [  # pattern for nouns
            {"pos": "NOUN"},
            {"pos": "ADP", "orth": "の"},
            {"pos": "NOUN", "orth": "たび"},
            {"orth": "に", "pos": "ADP"}
        ]
    ]

    matcher.add("tabini", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
