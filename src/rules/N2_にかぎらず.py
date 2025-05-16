import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2
"not just"; "not only...but also...", "not limited to..." 

Noun + に限らず

最近は、女性に限らず男性も化粧をする。
この映画は子供に限らず、大人も楽しめます。
この番組は若者に限らず老人も関心します。
ディズニー映画は子供に限らず、大人にも人気がある。
これから、科学に限らず文学もちゃんと勉強します。

'''


def match_nikagirazu_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # pattern with noun
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "に"},  # add optional argument for て form
            {"pos": "VERB", "lemma": {"IN": ["かぎる", "限る"]}},
            {"pos": "AUX", "lemma": "ず"}
          ],
    ]

    matcher.add("nikagirazu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
