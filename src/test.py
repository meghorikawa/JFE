# a method created to test the different functions.

import pipline
import json

text = "今日は！今日早く起きたの。"
processed_text = pipline.preprocess(text)

# Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")