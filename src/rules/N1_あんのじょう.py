

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1
"just as one thought" , "as usual" , "sure enough"

案の定、結果がよくないだ。
案の定、彼は第一位になった。
あの堤防は、案の定今回の台風で決壊してしまった。
急行は案の定混んでいて席がなかった。
案の定、レポートの提出の締め切りに間に合わなかった。
あの二人はけんかばかりしていて、案の定離婚した。
私の決意を家族に告げると,案の定皆さんがびっくりした。


'''
def match_annojyou_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": "案の定"},
        ],
        ]


    matcher.add("annojyou", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
