# main method I need to create separate line items for each participant and each writing.

# participant_writing num　


import spacy
from rules import rule_modules  # Dynamically import all rule files

nlp = spacy.load("ja_ginza")

def apply_matching(text):
    doc = nlp(text)  # Process text through pipeline first
    all_matches = {}

    for module_name, module in rule_modules.items():
        for attr in dir(module):
            if attr.startswith("match_"):
                match_func = getattr(module, attr)
                if callable(match_func):
                    all_matches[attr] = match_func(nlp, doc)
    print(f'Number of Forms: {len(rule_modules)}')
    return all_matches

# Example usage
text = ('''
夢みたいだ。
外は、夏みたいだよ。
あの人は、日本人みたいですね。日本語がペラペラでした。
子どもみたいに遊んだ。
私はお母さんみたいになりたい。
彼女は男の子みたいに元気がいい。
あなたみたいに美しい人は初めてだ。
彼女の心は氷みたいに冷たい。
バカみたいに見えるのは分かってる。
氷みたいに冷めたくしないでくれよ。
私も彼みたいに広い心を持ちたい。''')

results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")