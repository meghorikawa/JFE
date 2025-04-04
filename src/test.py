# a method created to test the different functions.

import pipline
import json

text = ("今日から自転車で出勤しよう。もう11時だ。早く寝よう。重たそうだね。手伝おうか。今日は食堂で昼食を食べよう。図書館で一緒に勉強しよう。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


