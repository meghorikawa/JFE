# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
うちの娘に限って、人をいじめるようなことはしません。
私は学校に休んだ日に限って、テストがある。
仕事が忙しい日に限って、なぜかシステムトラブルが発生する。
ここから富士山が見えるそうだけど、今日に限って雲が多いね。
彼は、いつも家にいるのに、今日に限って留守でした。
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
