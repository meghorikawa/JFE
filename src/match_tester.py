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
彼女は服が汚れるのもかまわず、公園で犬と遊んでいる。
あの男は人目もかまわず、電車の中で弁当を食べている。
あの二人は、みんなが見ているのもかまわず、キスをした。
彼は値段もかまわず、好きな料理をどんどん注文した。
病院であるのもかまわず、あの女性は携帯電話で大きな声で話している。
隣の人たちは近所の人の迷惑もかまわず毎晩遅くまで騒いでいる。
最近、電車の中で、人目もかまわず化粧をしている若い女性をよく見かける。
雨が降っていたが、ナナさんは濡れるのもかまわず走って帰ってしまった。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")