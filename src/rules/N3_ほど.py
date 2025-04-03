

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb (casual, non-past)	 + 程(ほど)
Noun
な-adjective + な
い-adjective


君ほど美しい人はいません！
今夜は凍えるほど寒い。
死ぬほどのどがかわいている。
今年ほど雨の降った年はなかった。

'''


def match_hodo_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for くらべる and くらべ form
            {"pos": {"IN":["ADP", "PART"]}, "lemma": {"IN":["ほど", "程"]}}, # allow for both hiragana and kanji

          ]
    ]

    matcher.add("hodo", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
