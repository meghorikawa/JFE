

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1
"A is better ", "Would rather A" 

VERB +　ほうがまし だ・です
NOUN+の+ ほうがまし　だ・です

gives clear superiority to at least two conflicting options

あなたと結婚するくらいなら、独身のほうがましだ。
ギャンブルに金を浪費するなら捨てたほうがましだ。
途中でやめるぐらいなら始めからやらないほうがましだ。
そんな雑誌を読むくらいなら、昼寝をするほうがましだよ。
こんな天気の中を出かけるよりは、家にいるほうがましだ。
これを彼にあげるなら捨ててしまったほうがましだ。
こんな苦しい思いをするくらいなら死んだほうがましだ。

'''
def match_hougamashi_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern with verb
            {},
            {"pos": "NOUN", "lemma": "ほう"},
            {"pos": "ADP", "lemma": "が"},
            {"pos": "ADJ", "lemma": "まし"},
        ],
        ]


    matcher.add("hougamashi", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
