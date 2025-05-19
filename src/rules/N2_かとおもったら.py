import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2
"just when I think...."; "no sooner than" 

Verb Form + た(past tense) + かと思ったら、かとおもうと、かと思えば


空が急に暗くなってきたかと思うと、雨が降ってきた。
うちの近くの公園の花が咲いたかと思ったら、もう散ってしまった
この時期は、晴れていたかと思えば、急に雨が降り出すことが多いから、傘をもっていったほうがいい。
さっきまで笑っていたかと思ったら、急に泣き出してしまった。
日曜日なのに、お父さんは忙しそうだね。さっき戻ったかと思うと、また出かけて行った。
彼は食事を始めたかと思ったら寝てしまった。

'''


def match_katoomottara_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern　
            {"pos": "VERB"},
            {"pos": "AUX", "lemma": "た"},
            {"pos": {"IN": ["PART","SCONJ"]}, "lemma": "か"},
            {"pos": "ADP", "lemma": "と"},
            {"pos": {"IN": ["VERB", "SCONJ"]}, "lemma": {["思う","おもう"]}},  # add optional argument for て form
            {"orth": {"IN": ["たら","と", "ば"]}},
        ],
    ]

    matcher.add("katoomottara", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
