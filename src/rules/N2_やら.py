

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"such things as A and B", "A and B and son on"
can also express uncertainty

AやらBやら

大学生は宿題やらアルバイトやらで忙しい。
さっきコンビニでおにぎりやらお茶やらを買った。
疲れやら空腹やらで、彼は死んだように倒れた。
サイクリングをする時は嬉しいやら楽しいやら、とてもいい気分だ。
カバンにはパソコンやらノートやら教科書やらが入っている。
両親からの仕送りは、家賃やら食費やらでほとんどなくなってしまった。
たくさんの蚊に食われて、かゆいやら痛いやらで大変だった。

'''
def match_yara_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADP", "lemma": "やら"},
        ],
        ]


    matcher.add("yara", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
