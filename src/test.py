# a method created to test the different functions.

import pipline
import json

text = ("今夜は凍えるほど寒い。死ぬほどのどがかわいている。今年ほど雨の降った年はなかった。。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


