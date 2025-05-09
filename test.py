# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''昨日、図書館に行ってレポートを書きました。
そして、友達と映画を見て、その後、食事をしました。
私が映画を見たことを覚えていると言いましたが、まだ食事に行っていません。歩きながら、食べるな！
''')
processed_text = pipeline.preprocess(text)

nlp = spacy.load("ja_ginza")
doc = nlp(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")
sentences = doc.sents
for sentence in sentences:
    clauses, subordinate, coordinate = clauseExtractor.extract_clauses(sentence)
    print(f' Clauses: {clauses}, Subordinate: {subordinate}, Coordinate: {coordinate}')
