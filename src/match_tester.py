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
毎日、一生懸命勉強したから、絶対合格するに決まっている。
同じ値段なら、質がいいほうがたくさん売れるに決まっている。
一人で外国へ旅行するなんて、親に反対されるに決まっている。
こんな暗いところで本を読んだら目に悪くなるに決まっている。
子供にそんなお菓子を見せたらほしがるに決まっている。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")