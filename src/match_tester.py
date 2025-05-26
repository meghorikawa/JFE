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
津波によって家という家が全て流されてしまった。
大雪で東京に行くの電車という電車が中止されている。
家に変な匂いがこもったので、窓という窓を全部開けた。
息子の部屋は壁という壁に車のポスターが貼ってある。
チラシをこの地域の家という家に配って歩いた。
今日という今日は、この仕事をやり遂げなければならない。
彼女は学校の規則をよそに爪という爪すべてを真っ赤に塗っていた。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")