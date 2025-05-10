# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
しばらくお待ち願います。
図書館では小さな声でお話し願います。
ご提案の詳細についてお聞かせ願えますか？
ご自分のシートベルトが安全にかかっているかお確かめ願います。
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
