

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"extremely", "dying to...", "cannot handle it"

VERB たくて form + たまらない
なadjective - な + で　＋たまらない
い adjective - い +くて　+　たまらない

あなたに会いたくてたまらない。
日本の夏は暑すぎてたまらない。
私は外国へ行きたくてたまらない。
子どものことが心配でたまらない。
私は目が痛くてたまらない。
彼女が出来て嬉しくてたまらない。
あの新しい映画を観たくてたまらない。

'''


def match_tetamaranai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "VERB"},
            {"pos": "AUX", "lemma":"たい", "OP": "?"},
            {"pos": "SCONJ", "lemma": "て"},
            {"pos": "VERB", "lemma": "たまる"},
            {"pos": "AUX", "lemma": {"IN": ["ない","ます"]}},
            {"pos": "AUX", "lemma": {"IN": ["ん", "ぬ"]}, "OP": "?"}# add masu form
        ],[ #adj pattern
            {"pos": "ADJ"},
            {"orth": {"IN": ["て","で"]}},
            {"pos": "VERB", "lemma": "たまる"},
            {"pos": "AUX", "lemma": {"IN": ["ない","ます"]}},
            {"pos": "AUX", "lemma": {"IN": ["ん", "ぬ"]}, "OP": "?"}# add masu form


            ]
        ]


    matcher.add("tetamaranai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
