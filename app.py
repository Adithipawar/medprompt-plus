import streamlit as st
from scripts.parser import extract_text
from scripts.summarizer import generate_summary
from scripts.explainer import extract_and_explain

st.set_page_config(page_title="MedPrompt", layout="wide")
st.title("🩺 MedPrompt: Medical Report Summarizer & Explainer")

uploaded_file = st.file_uploader("📄 Upload a Medical Report (PDF)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("⏳ Extracting text from PDF..."):
        extracted_text = extract_text(uploaded_file)

    st.subheader("📃 Extracted Report Text")
    st.write(extracted_text)

    if st.button("🧠 Generate Summary + Explanation"):
        with st.spinner("🔍 Summarizing medical report..."):
            summary = generate_summary(extracted_text)

        st.subheader("🔹 Summary")
        st.success(summary)

        with st.spinner("📚 Explaining Medical Terms..."):
            explanations = extract_and_explain(extracted_text)

        st.subheader("🔸 Medical Term Explanations")
        for term, explanation in explanations.items():
            st.markdown(f"**• {term.title()}**: {explanation}")
