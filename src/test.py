# a method created to test the different functions.

import pipline
import json

text = "この国の人口は減少する一方だと報告されています。感染症の拡大を防ぐためには、対策を強化する一方だろう。"
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


