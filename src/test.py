# a method created to test the different functions.

#import pipline
#import json

#text = "あまり肉をたべません。あまり肉を食べない"
#processed_text = pipline.preprocess(text)

# Save JSON
#with open("processed_text.json", "w", encoding="utf-8") as f:
#    json.dump(processed_text, f, ensure_ascii=False, indent=4)

#print("Processing complete! JSON saved.")

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
text = "この映画はあまり面白くない。私はあまり食べない。"
results = apply_matching(text)

for category, matches in results.items():
    print(f"{category}: {matches}")
