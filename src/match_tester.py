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
全員が参加しなければなりません。もっとも病気の場合は別です。
今回の失敗は田中さんの責任だ。もっとも、私たちも責任を一部持ちます。
検査の前夜から飲食禁止です。もっとも水は飲んでも構いません。
今年こそヨーロッパへ行きたいと思っています。もっとも休みが取れたらの話ですが。
今日の試合は私たちのチームが勝った。もっとも、次の試合はもっと難しいので無視にしないほうがいい。
ウィキペディアに全部書いてあるよ。もっともこのサイトは完全には信用できないけど。
関係ない人は書類をもらわないでください。もっとも、許可を持っている人がもらえます。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")