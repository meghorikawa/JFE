

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N1

"dare to", "daringly", "deliberately", "purposely"
used in context of something needless, unexpected or intentionally counterproductive

彼はあえて一人で行く気ですか。
私はあえて彼女に忠告した。
あえて彼の意見を支持した。
私は、あえて彼に電話をしない。
その時彼女はあえて何も言わなかった。
正社員じゃなく、あえてアルバイトとして働く人も多いです。
私だったらそれを思いのまま言うようなことはあえてしない。
最近は、車じゃなくてあえて自転車で通勤する人が増えている。

'''
def match_aete_N1(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": "ADV", "lemma": {"IN":["あえて", "敢えて"]}},
            {},
        ],
        ]


    matcher.add("aete", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
