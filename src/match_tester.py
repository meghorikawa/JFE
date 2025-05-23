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

これをいっぱい食べたら、病気の可能性があるよ。
その犬は暴れる可能性がある。
それは今後増える可能性があります。
このニュースレターを受け取った可能性があるのは誰ですか。
私はあなたにもその可能性があると思います。
あの行動が無駄になる可能性がある。
の会社は売り上げが減っているから、倒産の可能性がある。
それはこのままだと壊れる可能性がある。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")