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
ケンとマリは地図を見ているとき，家の犬はバスケットに飛びこんでしまいました。
彼たちはぜんぜんきけなくて、ピクニックに行きました．
芝生を座って，食べ物を食べたがったとき，バスケットを開うと，急に家の犬が現しました。
ビックリしました。
ケンとマリは食べられしまった食べ物を見たら，すごく悲しかったです。''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")