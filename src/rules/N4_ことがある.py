import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4

Verb (casual, non-past) +	ことがある
Verb (casual, non-past) +	こともある
Verb (casual, non-past) +	ことがあります
Verb (casual, non-past) +	こともあります

時々仕事をやめたいと思うことがある。
私の地元は6月でも寒いことがある。
普段は母がご飯を作りますが、私が作ることもあります。

'''


def match_kotogaaru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb adjective constructions use である which will also be caught.
            {"pos":"VERB"},
            {"lemma": "する", "pos": "AUX", "OP": "?"},  # optional auxiliary to account for する
            {"orth": {"IN" :["こと","事"]}, "pos": "NOUN", "OP": "?"},  # optional auxiliary to account for する
            {"orth": {"IN":["が","も"]}, "pos": "ADP"},
            {"lemma": "ある", "pos": "VERB"}, # use lemma to cature instances of polite form used also
        ]
    ]

    matcher.add("kotogaaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
