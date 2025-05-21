

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"this way", "in such a way", "how"

ふうに  + verb

こんなふうにやりなさい。
私もあんなふうになりたいです。
どういうふうに動くか見せてください。
すみません、これはどんなふうにやればよいでしょうか。
勝手にそんなふうにしないでください。教えたどおりにやればいいです。
彼の日本語がペラペラですね。私もあんなふうになりたいです。

'''
def match_fuuni_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos":"NOUN", "lemma": {"IN":["風", "ふう"]}},
            {"pos": "AUX", "orth": "に"},
            {"pos": "VERB"}
        ],
        ]


    matcher.add("fuuni", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
