

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

今まで以上に仕事を頑張ります。
必要以上にたくさんのお金を使わないでください。
私が予想していた以上に彼の様態はよくなかった。
今以上に日本語ができるようになりたいです。
私たちが泊まったホテルは、予想以上に豪華だった。
彼らは、わたしが考えた以上に強い反応を示した。


'''


def match_ijyouni_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "NOUN", "lemma": {"IN": ["いじょう", "以上"]}},
            {"pos": "ADP", "lemma": "に"}
          ],
    ]

    matcher.add("ijyouni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
