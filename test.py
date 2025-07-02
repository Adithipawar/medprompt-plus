import spacy

nlp = spacy.load("en_ner_bc5cdr_md")
doc = nlp("Patient has been diagnosed with COPD and prescribed prednisone.")

print([(ent.text, ent.label_) for ent in doc.ents])
