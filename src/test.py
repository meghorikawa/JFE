# a method created to test the different functions.

import pipline
import json

text = ("英語の文法は日本語ほど難しくありません。東京ほど家賃の高いところはない。私ほどあなたのことを大切に思っている人はいないだよ。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


