import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Verb ます (stem form)	やすい

日本語は分かりやすいです。
先生の声が聞きやすいです。
ひらがなは漢字より書きやすいです。
光に感じやすい。
彼女はカゼを引きやすいです。

'''


def match_yasui_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for　VERB stem + やすい
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": {"IN":["やすい", "易い"]}},
        ]
    ]

    matcher.add("yasui", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
