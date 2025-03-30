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

    return all_matches

# Example usage
text = ("環境破壊は年々進む一方だ。インターネットの普及により、オンラインサービスの需要が高まる一方です。この国の人口は減少する一方だと報告されています。都市部の住宅価格は上がる一方で、若者が家を買うのが難しくなっている。感染症の拡大を防ぐためには、対策を強化する一方だろう。")
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")