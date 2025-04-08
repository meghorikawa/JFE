import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4



Verb (casual)	ように / ような
Noun + の

お箸はこのように使います。
犬のように働いている。
その二人は燃えるような愛がありますね。
彼は家族のためだけに生きていたように思える。
見えるように、このパソコンはとても古いですがまだ使われている。
私を子どものように扱わないで。

'''


def match_youni_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for ように
            { },
            {"pos": {"IN": ["NOUN","AUX"]}, "lemma": "よう"},
            {"pos": "AUX", "orth": {"IN":["に","な"]}},
        ]
    ]

    matcher.add("youni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
