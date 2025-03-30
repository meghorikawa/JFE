import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N3

Verb ます (stem form)	切る ・切れる

どうしてそう言い切れるのですか。
長い小説を2日間で読み切った。

どうしてそう言い切れるのですか。長い小説を2日間で読み切った。今日はもう魚を全部売り切れた。それを食べ切れる？食べ切ります。


売り切る
言い切る　both seem to be set phrases and aren't parsed on their own when tokenized... make exceptions for them.
'''


def match_kiru_N3(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # Pattern for Verb (stem) + きる
            {"pos": "VERB", "tag": "動詞-一般"},
            {"lemma": {"IN": ["切る", "きる", "切れる", "きれる"]}, "tag": "動詞-非自立可能"},
            {"lemma": {"NOT_IN": ["ない"]}}  # Exclude negation
        ],
        [  # Pattern for exceptions of 言い切るand 売り切る。
            {"lemma": {"IN": ["言い切れる", "売り切れる"]}, "tag": "動詞-一般"},
            {"lemma": {"NOT_IN": ["ない"]}}  # Exclude negation
        ]
    ]

    matcher.add("kiru", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
