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
大学は、学生たちの要望にこたえて、図書館の利用時間を延ばした。
お客様の意見にこたえて、営業時間を延長することいたしました。
クライアントの要望にこたえて、新しい機能を追加いたしました。
多くのファンの声援にこたえる完璧なプレーをし遂げた。
我が社では消費者のニーズにこたえる新しい商品を開発中です。
両親の期待にこたえて、私はイギリスに留学した。
''')

doc = nlp(text)
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")