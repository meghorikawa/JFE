import spacy
from spacy.matcher import Matcher
from collections import Counter

# 安っぽい is tokenized as one word and won't be caught by this rule.....

'''
Level: N3

Verb (casual)	というより（も/は）
Noun
な-adjective
い-adjective

彼はかっこいいというよりかわいい。
彼は学者というよりは教師だ。
私の仕事は、仕事というより趣味に近い。
うちの子はこれができないというより、やる気がないと思う。
今日は涼しいというより寒いくらいだった。
今はラーメンというよりうどんが食べたい気分だ。
'''


def match_toiuyori_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [# noun pattern
            {"pos":"ADP", "orth":"と"},
            {"pos": "VERB", "lemma": {"IN": ["言う", "いう"]}},
            {"pos": "ADP", "lemma": "より"}
        ]
    ]

    matcher.add("toiuyori", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
