# a method created to test the different functions.

from src import pipeline, clauseExtractor
import json
import src.clauseExtractor
import spacy

text = ('''
この教科書の説明はわかりやすくて、しかも詳しい 。
今日はとても暑い。しかも、湿度も高いので何もしたくないだ。
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
