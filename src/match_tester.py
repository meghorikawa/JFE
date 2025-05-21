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
この小説は実際にあったことに基づいて書かれたそうです。
このテストの結果に基づいて君たちのクラスを分けるので、頑張ってください。
集めた資料に基づいて、卒業の論文を書きました。
私は長年の経験に基づき新入社員を教育する。
公務員の給与は、法律に基づいて決められています。
アンケート結果に基づいて、新商品の方向性を決めるつもりだ。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")