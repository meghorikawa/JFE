

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"can't help but...", "can't help but do..." 

VERB ない form + でいられない

試験の前だから、勉強しないではいられない。
態度悪いの店員に、一言文句を言わないではいられない。
友達がいじめられているところを見たので、何か言わないではいられなかった。
彼の真似を見るとおかしくて、笑わないではいられない。
台風 の影響が心配で、畑を見に行かないではいられなかった。
彼女はわからないことがあったら、辞書やインターネットですぐに調べないではいられない性格だ。


'''


def match_naidehairarenai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": {"IN": ["AUX", "VERB"]}, "lemma": "ない"},
            {"pos": "SCONJ", "orth":"で"},
            {"pos": "ADP", "lemma": "は"},
            {"pos": "VERB", "lemma": "いる"},
            {"pos": "AUX", "lemma": "られる"},
            {"pos": "AUX", "lemma": {"IN": ["ない","ます"]}}
        ],
        ]


    matcher.add("naidehairarenai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
