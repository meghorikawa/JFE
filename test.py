# a method created to test the different functions.

from src import pipeline
import json

text = ("死ぬほど、あなとのことがすき。野菜むりやりに食べさせられた。")
processed_text = pipeline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


