# a method created to test the different functions.

import pipline
import json

text = ("私の気持ちを言い切れなかった。この部屋に100人は入り切れない。いっぱい注文しないで、二人で食べ切れないから。このお酒は強すぎて、飲み切れなかった。")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


