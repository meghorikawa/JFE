import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N4



phrase + みたい(に・な)

子どもみたいに遊んだ。
私はお母さんみたいになりたい。
彼女は男の子みたいに元気がいい。
あなたみたいに美しい人は初めてだ。
彼女の心は氷みたいに冷たい。
バカみたいに見えるのは分かってる。
氷みたいに冷めたくしないでくれよ。
私も彼みたいに広い心を持ちたい。

'''


def match_mitaini_N4(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for みたい に・な
            {},
            {"pos": "AUX", "lemma": "みたい"},
            {"pos": "AUX","orth": {"IN":["に","な"]}},
            {}
        ]
    ]

    matcher.add("mitaini", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
