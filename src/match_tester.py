# this is a python script to test the matcher as I continue implementation.
# I am keeping this separate from the main method for now
import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text first
    all_matches = {}

    for module_name, module in rule_modules.items():
        for attr in dir(module):
            if attr.startswith("match_"):
                match_func = getattr(module, attr)
                if callable(match_func):
                    all_matches[attr] = match_func(nlp, doc)
    #print(f'Number of Forms: {len(rule_modules)}')
    return all_matches

# Example usage
text = ('''

彼が犯人だったとは…
才能のある彼女が急に亡くなるとは、とても残念です。
自分だけで日本語を勉強して、あそこまで会話が上手とはすごいなあ。
サンフランシスコは家賃が高いと聞いていたが、こんなに高いとは驚きだ。
彼女がオリンピックで金メダルを取るとは誰も予想しなかった。
あんなに女らしく美しく見える人が、実は男だったとは…
妹の結婚式に出られないとは、残念な限りだ。
JLPTとはJapanese Language Proficiency Test の略で、日本語能力試験のことである。
今まで明かされなかった衝撃の真実とは…

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")