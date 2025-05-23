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
目覚まし時計が壊れたもんだから、遅刻してしまった。
すみません、風邪を引いてしまったものですから、今日は欠席です。
上着を着たままですみません。寒いものだから。
すみません。お酒は苦手なものですから。
一人っ子なものだからわがままに育ててしまいました。
遅くなってごめんなさい。道路が混んでいたものだから。
上着を脱いでもいいですか？熱いものですから。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")