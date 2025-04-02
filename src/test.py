# a method created to test the different functions.

import pipline
import json

text = ("先生の答えがいつも正しいとは限りません。こういう音楽は誰でも好きだとは限らない。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


