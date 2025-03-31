# a method created to test the different functions.

import pipline
import json

text = ("あなたのことは決して忘れません。私は決して夢をあきらめない。決してあなたは一人じゃありません。社長には、決して失礼な言葉を言ってはいけません。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


