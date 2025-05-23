

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"any kind of", "whatever"

いかなる　如何なる

君はいかなる状況でも部屋を離れてはならない。
私はいかなる質問にも答えるつもりはない。
警察はいつもいかなる事態にも対処できる態勢にある。
私たちはいかなる損害にもその責任を負いません。
彼はいかなる難局にも処しうる男だ。
彼女はいかなる困難にであっても、気を落とすことはない。
我々はいかなる犠牲をはらっても目標を達成せねばならぬ。


'''
def match_ikanaru_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {"pos": "ADJ", "lemma": {"IN": ["如何なる","いかなる"]}},
            {"pos":{"IN":["NOUN","ADJ"]}},
        ],
        ]


    matcher.add("ikanaru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
