# 🩺 MedPrompt: Medical Report Summarization + Explanation

**MedPrompt** is a generative AI-powered application that simplifies complex medical reports into plain English and explains key medical terms using Wikipedia.  
This app is built for patients, caregivers, and healthcare professionals to make medical diagnostics more understandable.


## 🚀 Features

- **PDF/Text Upload**: Upload `.pdf` or `.txt` medical reports.
- **Summarization**: Summarizes reports using a fine-tuned **T5** model.
- **Medical Term Extraction**: Uses **SciSpacy's biomedical NER** to extract diseases and medications.
- **Explanation**: Provides plain-English definitions of terms via **Wikipedia**.
- **Streamlit UI**: Interactive and user-friendly frontend.


## Project Structure

medprompt-plus/
├── app.py                      # Streamlit frontend
├── requirements.txt            # Python dependencies
├── README.md                 
│
├── scripts/                    # Core functionality
│   ├── parser.py               # PDF/TXT file reader
│   ├── summarizer.py           # Summarization (T5)
│   └── explainer.py            # Medical NER + Wikipedia
│
├── content/                    # Fine-tuned T5 summarization model
│   └── medprompt_model/
│       ├── config.json
│       ├── model.safetensors
│       └── ...
│
├── training_data/              # Data used for model fine-tuning
│   └── med_dataset_expanded.csv
│
├── sample_inputs/              # Sample reports for testing
│   ├── sample_report.pdf
│   └── ...


## Installation & Setup

### 1. **Clone the repository**

git clone https://github.com/yourusername/medprompt-plus.git
cd medprompt-plus

### 2. **Create a virtual environment**

python3 -m venv venv
source venv/bin/activate

### 3. **Install dependencies**

pip install -r requirements.txt

### 4. **Run the app**

streamlit run app.py

## Training Dataset

The summarization model was trained using a small biomedical dataset located at:

training_data/med_dataset_expanded.csv

## Model Info

Base Model: T5-small
Fine-Tuned On: Custom summarization dataset on Google Colab
NER Model: SciSpacy - en_ner_bc5cdr_md



