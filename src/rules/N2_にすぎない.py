

import spacy
from spacy.matcher import Matcher
from collections import Counter

'''
Level: N2

"Merely", "no more than" 

Casual Verb/ Noun(である)/ なadjective (である)/ いadjective に過ぎない　・ に過ぎません

単に幸運だったにすぎない。
これはまだ始まりにすぎない。
そんなのは言い訳に過ぎない。
それはただの道具にすぎない。その道具をどう使うかが大切だ。
病気で病院へ行ったといっても、ただの風邪に過ぎない。
私はこの会社の一社員にすぎませんから、決定権はありません。
いくら働いても一ヶ月の収入は２０万円にすぎない。
'''
def match_nisuginai_N2(nlp, doc):
    matcher = Matcher(nlp.vocab)

    patterns = [
        [  # general pattern for verb
            {"pos": "ADP", "lemma": "に"},
            {"pos": "VERB", "lemma": {"IN": ["過ぎる","すぎる"]}},
            {"pos": "AUX", "lemma": {"IN": ["ます","ない"]}},
        ],
        ]


    matcher.add("nisuginai", patterns)
    matches = matcher(doc)

    # Count occurrences
    match_counts = Counter()
    for match_id, start, end in matches:
        match_text = doc[start:end].text
        match_counts[match_text] += 1

    return dict(match_counts)
