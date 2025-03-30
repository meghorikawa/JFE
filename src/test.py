# a method created to test the different functions.

import pipline
import json

text = ("綺麗なお陰で、掃除が楽でした。狭いおかげで、あまり人呼べない。今日、皆さんのおかげで私の夢を実現しました。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


