# a method created to test the different functions.

import pipline
import json

text = ("背が高いくせに早く走れない。元気なくせに、病気のふりをしている。医者でもないくせに。彼女はお金持ちのくせにケチだ")
processed_text = pipline.preprocess(text)

#Save JSON
with open("processed_text.json", "w", encoding="utf-8") as f:
    json.dump(processed_text, f, ensure_ascii=False, indent=4)

print("Processing complete! JSON saved.")


