import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

to want to do ~

verb - ます + たい

日本語をもっと勉強したいです。
先生、聞きたいことがありますが。
子どものころから、ずっと日本に行きたかった。
つかれたから、もう勉強したくない。
'''


def match_tai_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["AUX","VERB"]}},
            {"pos": "AUX", "lemma": "たい"},
            {},
          ],
    ]

    matcher.add("tai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
