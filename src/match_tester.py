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
あなたと結婚するくらいなら、独身のほうがましだ。
ギャンブルに金を浪費するなら捨てたほうがましだ。
途中でやめるぐらいなら始めからやらないほうがましだ。
そんな雑誌を読むくらいなら、昼寝をするほうがましだよ。
こんな天気の中を出かけるよりは、家にいるほうがましだ。
これを彼にあげるなら捨ててしまったほうがましだ。
こんな苦しい思いをするくらいなら死んだほうがましだ。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")