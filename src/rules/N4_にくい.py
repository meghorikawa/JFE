import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4



Verb ます (stem form)	にくい

箸は使いにくいです
この質問には答えにくいです。
この本は字が小さくて読みにくいです。
この漢字は覚えにくいです。
この自転車は古くて乗りにくいです。
魚は骨が多くて食べにくいだ。
彼の説明が難しくて分かりにくいだった。
この道は狭くて、車も多いので、運転しにくいです。
'''


def match_nikui_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for にくい
            {"pos": {"IN" : ["VERB","AUX"]}},
            {"pos": "AUX", "lemma": "にくい"},
        ]
    ]

    matcher.add("nikui", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
