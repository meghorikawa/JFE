import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N5

must do; need to do

verb ない-い + くてはいけない
                くてはいけません

本当にすぐ行かなくてはいけない。
急がなくてはいけない。
もう10時だ。寝なくてはいけない。
日本語をもっと勉強しなくてはいけない。
花の水やりをしなくてはいけません。

'''


def match_nakutehaikenai_N5(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {},
            {"pos": "AUX", "lemma": "ない"},
            {"pos": "SCONJ", "lemma": "て"},
            {"pos": "ADP", "lemma": "は"},
            {"pos": "VERB", "lemma": {"IN" : ["行ける","いける"]}},
            {"pos": "AUX", "lemma": {"IN": ["ます", "ない"]}}
          ],
    ]

    matcher.add("nakutehaikenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
