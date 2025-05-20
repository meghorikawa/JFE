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
毎日遅くまで残業しているから、疲れて当然だ。
人間だから間違いがあって当然です。そんなに落ち込まないでください。
マンションの近くに電車が走っているから、うるさくて当たり前だ。
今回のテストはとても簡単なので満点が取れて当然です。
女性だから料理ができて当たり前だと思わないでください。
彼女はいつも人の悪口ばかり言っているので、みんなに嫌われて当然だ。
マンションの近くに電車が走っているから、うるさくて当たり前だ。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")