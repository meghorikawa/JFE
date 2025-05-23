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
優勝できたのは、チーム全員の協力あればこそだ。
家族を愛すればこそ、自分が犠牲になることなどは恐れない。
子供のためを思えばこそ、費用は子ども自身に用意させたのです。
自分の努力を認めてくれる人がいればこそ、やる気も出てくるというものだ。
忙しければこそ、時間の使い方が上手になってくるものだ。
夜中に一人で歩いて帰れるのも、この街が安全であればこそだ。
娘の将来を思えばこそ、彼との結婚には賛成できない。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")