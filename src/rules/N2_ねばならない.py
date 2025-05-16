import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2
"have to do; must; should~"

Neg. Verb - ない + ねばならない , ねばなりません

歯医者に行かねばならない。
9時までに戻らねばならない。
ビザが切れたので、国に帰らねばならない。
来月から、転勤で北海道へ行かねばならない。
地球を守るために、プラスチック製品を減らさねばならない。

'''


def match_nebanaranai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # pattern with noun
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "ぬ"},  # add optional argument for て form
            {"pos": "SCONJ", "lemma": "ば"},
            {"pos": "VERB", "lemma": {"IN": ["なる", "なり"]}},
            {"pos": "AUX", "lemma": {"IN":["ない", "ます"]}},
            {"pos": "AUX", "lemma": "ぬ", "OP": "?"},
          ],
    ]

    matcher.add("nebanaranai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
