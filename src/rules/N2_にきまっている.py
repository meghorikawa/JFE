

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"I'm certain...", "It's definitely the case...."

NOUN/ADJ/VERB +に決まっている

毎日、一生懸命勉強したから、絶対合格するに決まっている。
同じ値段なら、質がいいほうがたくさん売れるに決まっている。
一人で外国へ旅行するなんて、親に反対されるに決まっている。
こんな暗いところで本を読んだら目に悪くなるに決まっている。
子供にそんなお菓子を見せたらほしがるに決まっている。


'''


def match_nikimatteiru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN": ["きまる","決まる"]}},
            {"pos": "SCONJ", "lemma": "て"},
            {"pos": "VERB", "lemma": "いる"},
        ],
        ]


    matcher.add("nikimatteiru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
