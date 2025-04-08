import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4



phrase + みたい（だ）

夢みたいだ。
外は、夏みたいだよ。
あの人は、日本人みたいですね。日本語がペラペラでした。

'''


def match_mitai_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for みたい だ
            { },
            {"pos": "AUX", "lemma": "みたい"},
            {"orth": {"NOT_IN":["に","な"]}},
        ]
    ]

    matcher.add("mitai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
