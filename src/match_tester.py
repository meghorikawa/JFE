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
教師とはいえ、答えられないこともある。
分かっているとはいえ、やっぱり別れは辛いものだ。
私は日本人だとはいえ、アメリカで育ったので、漢字があまり読めません。
まだ締め切りまで時間があるとはいえ、早めに完成したほうがいい。
もう過去のこととはいえ、そう簡単には許すことはできない。
知らなかったこととはいえ失礼なことをしてしまい、大変申し訳ありませんでした。
入社したばかりとはいえ、もう少しまともな挨拶が出来ないのだろうか。
彼はまだ未成年だとはいえ、自分の犯した行為にしっかりと責任を持つべきだ。

''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")