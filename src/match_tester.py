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
このバスは距離にかかわらず、どこまで行っても200円だ。
値段にかかわらず、新しいiPhoneが発売したら買うつもりだ。
明日の国際交流イベントに来る来ないにかかわらず、連絡してください。
お酒を飲む飲まないに関わらず、飲み会の参加費は3,000円です。
好き嫌いに関わらず、家族のためにこの仕事は必ずしなければならない。
テストの点数に関わらず、間違えたところは復習するようにしてください。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")