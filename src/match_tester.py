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
かなり多くの人々が今なおそれを信じている。
とても寒く、なお悪いことに、雨が降り始めた。
今度の打ち合わせは土曜日です。なお、時間は後ほどお伝えします。
あとで起こったことはなお悪かった。
この件の説明は以上です。なお、詳細についてプリントをご覧ください。
この試合に申し込むとき、履歴書を提出してください。なお参加費も提出してください。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")