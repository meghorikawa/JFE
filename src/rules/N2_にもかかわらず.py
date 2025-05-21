

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"despite", "in spite of", "although~"

NOUN/adj/verb にかかわらず（関わらず）

大学生にも関わらず、基本的な漢字が書けない人もいる。
問題が易しかったにも関わらず、不注意でミスをしてしまった。
一生懸命勉強したにも関わらず、入りたかった大学の試験に落ちてしまった。
彼は全く日本語が話せないにも関わらず、日本で生活したいと言っている。
校則で禁止されているにも関わらず、授業中にスマホを使う学生が多い。
彼女は日本語が上手であるにも関わらず、日本人と会話する時はいつも英語を使う。

'''
def match_nimokakawarazu_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": {"IN": ["ADP","SCONJ"]}, "lemma": "に"},
            {"pos": {"IN": ["SCONJ","ADP"]}, "lemma":"も"},
            {"pos": "SCONJ", "lemma": {"IN": ["関わる","かかわる"]}},
            {"pos": "SCONJ", "orth": "ず" },
        ],
        ]


    matcher.add("nimokakawarazu", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
