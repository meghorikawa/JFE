# this is an additional file to re-organize the corpus and add additional writings that were added for a storytelling
# task.


import os
import shutil
import re

# make a list of the current participants writings
participant_list = os.listdir("/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/Corpus")

new_writings_list = os.listdir("/Users/megu/Desktop/corpus_add")

writings_dir = "/Users/megu/Desktop/corpus_add"
corpus_dir = "/Users/megu/Documents/Tübingen Universität/Thesis/FeatureExtractor/Corpus"


def copy_new_writings(writings_dir):
    for filename in os.listdir(writings_dir):
        if filename.endswith(".txt"):
            try:
                # change filename
                normalized_filename = filename.replace("-", "_")
                # parse filename
                participant_name, task = filename.split("-")
                task = task.replace(".txt", "")
                participant_path = os.path.join(corpus_dir, participant_name)

                # if directory doesn't exist create it
                os.makedirs(participant_path, exist_ok=True)

                # source and destination paths
                src_path = os.path.join(writings_dir, filename)
                dst_path = os.path.join(participant_path, normalized_filename)

                clean_writings(src_path, dst_path)

            except Exception as e:
                print(f"{filename} failed {e}")


def clean_writings(input_file_path, output_path):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Open Original file
    with open(input_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # remove corrections in the Sw1 files (I am removing this as it isn't included in all of the files and
    # the rest of the corpus is uncorrected as well.

    # Remove anything in parentheses — both ASCII () and full-width （）
    content = re.sub(r"\([^)]*\)", "", content)  # half-width ()
    content = re.sub(r"（[^）]*）", "", content)  # full-width （）

    # remove line labels like CCH02-SW1-00010-K
    # Remove line labels like CCH03-SW1-00010-K<TAB>
    content = re.sub(r"^[^\t]*\t", "", content, flags=re.MULTILINE)

    # write cleaned text to the corpus directory
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        f.close()
    print(f"Copied and cleaned {input_file_path} to {output_path}")

# clean the corpus texts
for participant_name in participant_list:
    participant_path = os.path.join(corpus_dir, participant_name)
    if not os.path.isdir(participant_path):
        continue
    docs_list = os.listdir(participant_path)
    for doc in docs_list:
        doc_path = os.path.join(participant_path, doc)
        clean_writings(doc_path, f"/Users/megu/Desktop/cleaned_corpus/{participant_name}/{doc}")


# additionally pull mother tongue data and J-cat score from the participant data list
