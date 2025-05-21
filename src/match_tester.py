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
今日、やく2週間ぶりに雨が降った。
この街に帰ってくるのはもう１０年ぶりだなあ。
先週からずっと雨が降った。一週間ぶりにようやく晴れてきた。
父はうちで倒れて入院したが、意識がなかった。二日ぶりに意識を回復した。
高校を卒業してから、2年ぶりにクラスメイトに会った。
最近はずっと忙しかったが、今日は久しぶりにゆっくり休むことが出来た。
今日、3ヶ月ぶりにまた北海道へ出張しに行ってきました。
台風で電車が不通になっていたが、10時間ぶりに運転を始めたそうだ。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")