import spacy
import wikipedia

# Load the BC5CDR model (disease and chemical NER)
nlp = spacy.load("en_ner_bc5cdr_md")

def extract_medical_terms(text):
    """
    Extracts medical terms (diseases and chemicals) from text using SciSpacy.
    """
    doc = nlp(text)
    terms = set(ent.text.strip().lower() for ent in doc.ents)
    return list(terms)

def explain_terms(terms):
    """
    Fetches Wikipedia summaries for each extracted medical term.
    """
    explanations = {}
    for term in terms:
        try:
            summary = wikipedia.summary(term, sentences=2)
            explanations[term] = summary
        except wikipedia.exceptions.DisambiguationError as e:
            explanations[term] = f"Multiple meanings found: {e.options[:2]}"
        except wikipedia.exceptions.PageError:
            explanations[term] = "❌ No Wikipedia page found."
        except Exception as e:
            explanations[term] = f"⚠️ Error: {str(e)}"
    return explanations

def extract_and_explain(text):
    """
    Complete pipeline: extract terms and explain them.
    """
    terms = extract_medical_terms(text)
    return explain_terms(terms)
