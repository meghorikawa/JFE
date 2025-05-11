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
梅雨に入ってからほとんど雨が降っていない。このまま降らないと、水不足になる恐れがある。
大きい地震が来たら、この建物は倒れる恐れがある。
この番組は子供に悪い影響を与える恐れがある。
台風がこのまま北上すると、日本に上陸する恐れがある。
こんなに赤字が続くと、この会社は倒産の恐れがある。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")