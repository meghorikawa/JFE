

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"unable to ..." ; "can't afford to ..." 

Phrase と考えられる（考えられます）

これは今年最高の映画だと考えられている。
彼が死んだ原因は事故だと考えられる。
彼女は優秀な医者であると考えられている。
このデータは今後の研究に役に立つと考えられる。
その事故はスピードの出しすぎのせいだと考えられます。

'''


def match_tokangaerareru_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADP", "lemma": "と"},
            {"pos": "VERB", "lemma": {"IN": ["考える","かんがえる"]}},
            {"pos": "AUX", "lemma": "られる"},
        ],
        ]


    matcher.add("tokangaerareru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
