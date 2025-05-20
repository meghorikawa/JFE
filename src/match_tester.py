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
私はそれが気になってしょうがない。
今日は寒くてしょうがない。
今日は何もすることがなくて、暇で仕方がない。
お金をくれて、嬉しくてしょうがない。
バスで行くのは、時間がかかってしょうがない。
海外で一人暮らしを始めたばかりなので、寂しくてしかたがありません。
最近はやることがないので、毎日が暇でしかたがない。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")