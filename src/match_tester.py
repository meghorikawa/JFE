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
text = ('''ご注文は以上ですか？
６歳以上の子どもはがっこうに通わなければならない。
私からは以上でございます。
今まで以上に仕事を頑張ります。
必要以上にたくさんのお金を使わないでください。
私が予想していた以上に彼の様態はよくなかった。
今以上に日本語ができるようになりたいです。
私たちが泊まったホテルは、予想以上に豪華だった。
彼らは、わたしが考えた以上に強い反応を示した。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")