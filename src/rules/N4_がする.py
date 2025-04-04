import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4


Noun	+   がする
            がします
            がしている

甘い味がする。
人の声がする。
ガスの匂いがする。
このクッキーはしょうがの味がする。
このフルーツはどんな味がする？

'''


def match_gasuru_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for verb
            {"pos": "NOUN"},
            {"pos": "ADP", "orth": "が"},
            {"lemma": "する", "pos": "VERB"},
        ]
    ]

    matcher.add("gasuru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
