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
明日は、雨が降らない限り、10時に学校で会いましょう。
この仕事は、私が生きている限り、ずっと続けていきたい。
私の知っている限りでは、彼女はまだ結婚していません。
学生である限り、学割が使えます。
日本にいる限り、日本語が必要だよ。
今のやり方を変えない限り、悪い状況は続くでしょう。
お店の中にお客様がいる限り、お店は閉めません。
悪い生活習慣を改めない限り、健康にはなれない。
自分の歌を聞いてくれる人がいる限り、路上で歌たい続けようと思います。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")