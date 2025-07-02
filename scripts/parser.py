import fitz  # PyMuPDF
import io

def extract_text(uploaded_file):
    """
    Extracts text from a Streamlit UploadedFile object (.pdf or .txt).
    """
    filename = uploaded_file.name.lower()

    # Handle PDF files
    if filename.endswith(".pdf"):
        pdf_bytes = uploaded_file.read()
        text = ""
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text

    # Handle TXT files
    elif filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        return "Unsupported file format. Please upload a .pdf or .txt file."
