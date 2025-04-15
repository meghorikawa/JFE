## method to handle the pipeline for text pre-processing

import spacy



# method to process document and output in JSON format for easy feature parsing.
def preprocess(text):
    #for now save text as json format seperated by sentences

    # Load the GiNZA model
    nlp = spacy.load("ja_ginza")
    doc = nlp(text)

    # output format
    output = [{ "paragraphs": [{
        "raw_text": text,
        "sentences": []
        }]
    }]

    for sent in doc.sents:
        sentence_data = {
            "tokens": []
        }
        for token in sent:
            # get reading of token
            reading = token.morph.get("Reading")[0]
            token_data = {
                "id":token.i +1,
                "orth":token.text, # the actual written token
                "reading": reading, # pronunciation this however only returns most common and not necessarily based
                # on context.....
                "lemma":token.lemma_, # lemma (dictionary form)
                "pos": token.pos_,
                "tag":token.tag_, # detailed pos tag
                "dep":token.dep_,
                "head":token.head.i + 1 if token.head != token else 0, # dependency head
                "inflection": token.morph.get("Inflection"),
            }
            sentence_data["tokens"].append(token_data)
        output[0]["paragraphs"][0]["sentences"].append(sentence_data)
    return output


