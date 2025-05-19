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
我々が成功できるかどうかは君次第だ。
花火大会は天気次第で中止になる場合もあります。
結婚した相手次第で人生が決まってしまうこともある。
部屋の準備ができ次第、会議を始めます。
雨がやみ次第、出発することにしましょう。
詳しいことは情報が入り次第、お伝えします。
式が終了次第、ロビーに集合してください。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")