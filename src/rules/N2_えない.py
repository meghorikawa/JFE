

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2


あの人が結婚したって本当！？え～！あり得ないよ！
あの真面目な彼が犯人？そんなことはあり得ない。
地震がいつ来るかなんて、予測し得ないことだ。
無から有は生じ得ない。
機械は完全には人力に代わり得ない。
このような困難な仕事は、我々の力だけでは処理し得ない。
今回は予測し得ないことが起きたけど、皆さんは落ち着いてください。


'''


def match_enai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern
            {"pos": {"IN": ["VERB", "AUX"]}},
            {"pos": "VERB", "lemma": {"IN": ["得る", "える"]}},
            {"pos": "AUX", "lemma": "ない"},
          ],
    ]

    matcher.add("enai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
