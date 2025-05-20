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
走れば間に合わないことはないよ。急ごう！
嬉しくないことはないが、1位が良かった。
車を運転できないことはないんですが、ほとんどしません。
鶏肉は、食べないことはないですが、あまり好きではありません。
できないことはないですけど、少し時間をいただきたいです。
私も留学したことがありますから、あなたの苦労が分からないことはありません。
これは美味しくないことはないですけど、家の近くのラーメン店の方が安くて美味しいです。
私も留学したことがありますから、あなたの苦労が分からないことはありません。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")