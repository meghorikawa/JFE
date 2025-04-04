import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


phrase +    かしら (feminin)

本当かしら。
どこへ行ったかしら。
誰かしら。
彼は本気かしら。
明日は雨かしら。
この本は売れるかしら？
明日は晴れるかしら。

'''


def match_kashira_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb
            {"lemma": "かしら", "pos": "PART"},
        ]
    ]

    matcher.add("kashira", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
