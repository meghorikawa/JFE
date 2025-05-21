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
果たしてそうだろうか。
果たして本当に足音が聞こえたのかどうかはわからない。
そのうわさは果たして本当だろうか。
私があの店にいるとき、彼らがそこにやってきたのは果たして偶然だろうか？
この程度の金額で、果たして彼が承知するだろうか。
皆さんにも果たしていただく役割があります。
機械には特に悪いところがないと、果たして何が故障の原因だったのだろうか。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")