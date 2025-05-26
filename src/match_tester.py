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

後輩なら先輩に敬語を使ってしかるべきだ。
退学する前に、親と相談してしかるべきだ。
この小説はもっと評価されてしかるべきだ。こんなに面白い本は読んだことがない。
この道には車がたくさん通っているのだから、信号があってしかるべきだ。
状況が変わったのだから、会社の経営計画も見直されてしかるべきだ。
優秀な学生には奨学金が与えられてしかるべきだ。
女性は料理ができてしかるべきだという考え方は古い。
老人のための国立の病院がもっとあってしかるべきだ。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")