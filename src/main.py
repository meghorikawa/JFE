# main method I need to create separate line items for each participant and each writing.

# participant_writing num　


import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text through pipeline first
    all_matches = {}

    for module_name, module in rule_modules.items():
        for attr in dir(module):
            if attr.startswith("match_"):
                match_func = getattr(module, attr)
                if callable(match_func):
                    all_matches[attr] = match_func(nlp, doc)

    return all_matches

# Example usage
text = ('''
今起きたところです。
昼ごはんを食べたところです。
アメリカから日本に戻ったところです。
駅に着いた時、ちょうど電車が出たところでした。
あなたのことを話したところだよ。
図書館にあなたを探しに行ったところです。
私は今起きたばかりです。
ずいぶん長くかかったのね。心配になっていたところよ。
この仕事を始めたばかりです。
田中さんは先月にこの会社に入ったばかりです。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")