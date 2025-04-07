# a method created to test the different functions.

import pipline
import json

text = ("彼は入院しているところです。今料理をしているところです。私は今、家で日本語を勉強しているところです。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


