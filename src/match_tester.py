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
案の定、結果がよくないだ。
案の定、彼は第一位になった。
あの堤防は、案の定今回の台風で決壊してしまった。
急行は案の定混んでいて席がなかった。
案の定、レポートの提出の締め切りに間に合わなかった。
あの二人はけんかばかりしていて、案の定離婚した。
私の決意を家族に告げると,案の定皆さんがびっくりした。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")