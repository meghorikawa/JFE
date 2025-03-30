# a method created to test the different functions.

import pipline
import json

text = ("彼は人の名前を忘れ気味である。昨夜、彼は風邪気味だった。風邪気味で、熱っぽいんだ。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


