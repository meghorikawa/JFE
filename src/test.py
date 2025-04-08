# a method created to test the different functions.

import pipline
import json

text = ("外は、夏みたいだよ。あの人は、日本人みたいですね。日本語がペラペラでした。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


