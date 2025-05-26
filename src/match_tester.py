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

遅刻するの場合は先生もしくは僕に連絡してください。
お問い合わせは、電話もしくはファックスでお願いします。
あの男は弁護士もしくは裁判官ですか。
参加費はクレジットカードもしくは現金で払うことができます。
この施設は、会員もしくはその家族に限り使用できる。
明日は社長もしくは部長が新計画を発表なさります。
同封の許可証にご両親もしくは保護者の同意署名をもらってください。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")