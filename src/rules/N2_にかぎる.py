import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"Nothing beats...." 

寒い日は、熱いラーメンに限る。
風邪には寝ているに限る。
何といっても我が家に限る。
夏は冷たいビールに限る。

'''


def match_nikaigiru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "VERB"},
            {"POS": {"IN": ["AUX", "SCONJ", "VERB"]}, "OP": "*"}, #allow for auxilaries to be added
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN": ["かぎる", "限る"]}},
            {"pos":"SCONJ", "lemma": {"NOT_IN": ["て"]}}
          ],[  # pattern with noun
            {"pos": "NOUN"},
            {"pos": "ADP", "lemma": "に"},  # add optional argument for て form
            {"pos": "VERB", "lemma": {"IN": ["かぎる", "限る"]}},
          ],
    ]

    matcher.add("nikagiru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
