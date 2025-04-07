# a method created to test the different functions.

import pipline
import json

text = ("図書館にあなたを探しに行ったところです。私は今起きたばかりです。ずいぶん長くかかったのね。心配になっていたところよ。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


