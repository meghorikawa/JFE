# a method created to test the different functions.

import pipline
import json

text = ("やるしかない。歩くしかなかった。毎日勉強するしかないですよ。もう両親に頼むしかありません。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


