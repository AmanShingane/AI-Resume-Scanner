# 📄 AI Resume Scanner

An intelligent resume screening system that matches candidate resumes against a job description using **NLP embeddings** and **cosine similarity** — built with Streamlit and deployed on Streamlit Cloud.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resume-scanner-deqguxfruf4r6sds6wxfyd.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red)
![sentence-transformers](https://img.shields.io/badge/sentence--transformers-2.7.0-green)

---

## 🧠 Overview

The **AI Resume Scanner** automates the initial resume screening process by:

- Extracting text from uploaded PDF resumes
- Preprocessing and cleaning both the resume and job description text
- Generating semantic embeddings using **Sentence Transformers**
- Computing cosine similarity between each resume and the job description
- Extracting key skills from each resume
- Ranking all candidates by match score in a sortable table

---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 Bulk Upload | Upload multiple PDF resumes at once |
| 🔍 Semantic Matching | Uses sentence embeddings (not just keyword matching) |
| 📊 Match Score | Cosine similarity score for each resume vs job description |
| 🛠️ Skill Extraction | Automatically extracts skills mentioned in each resume |
| 📋 Ranked Results | Candidates sorted by match score (highest first) |
| ☁️ Cloud Ready | Deployable on Streamlit Community Cloud |

---

## 🗂️ Project Structure

```
AI-Resume-Scanner/
├── app.py                  # Main Streamlit application
├── src/
│   ├── parser.py           # PDF text extraction
│   ├── preprocess.py       # Text cleaning & normalisation
│   ├── vectorizer.py       # Sentence embedding generation
│   ├── matcher.py          # Cosine similarity calculation
│   └── skill_extractor.py  # Skills extraction from text
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level packages (for Streamlit Cloud)
├── runtime.txt             # Python runtime version
└── README.md
```

---

## ⚙️ How It Works

```
Job Description ──► Preprocess ──► Embedding ──┐
                                                ├──► Cosine Similarity ──► Ranked Results
PDF Resume      ──► Extract ──► Preprocess ──► Embedding
                                     └──────────────────► Skill Extraction
```

1. **Parse** — `pdfplumber` / `PyMuPDF` extracts raw text from each PDF resume
2. **Preprocess** — NLTK cleans and normalises text (lowercasing, stopword removal, lemmatisation)
3. **Embed** — `sentence-transformers` converts text into dense semantic vectors
4. **Match** — `scikit-learn` computes cosine similarity between the JD and each resume
5. **Extract** — Skills are identified and listed alongside each candidate
6. **Rank** — Results are sorted by score and displayed in a pandas DataFrame

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/AmanShingane/AI-Resume-Scanner.git
cd AI-Resume-Scanner
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501**.

---

## ☁️ Deploy on Streamlit Cloud

1. Push the repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo, set `app.py` as the entry point
4. Click **Deploy**

> `packages.txt` and `runtime.txt` are already configured for Streamlit Cloud — no extra setup needed.

---

## 📦 Dependencies

```
streamlit==1.45.1
pandas==2.2.3
numpy==1.26.4
scikit-learn==1.5.2
sentence-transformers==2.7.0
transformers==4.41.2
torch==2.1.2
pdfplumber==0.11.6
python-docx==1.1.2
nltk==3.9.1
PyMuPDF==1.26.0
```

---

## 🖥️ Usage

1. **Paste** the job description into the text area
2. **Upload** one or more PDF resumes using the file uploader
3. Click **Screen Resumes**
4. View the ranked results table showing each candidate's **Match Score** and extracted **Skills**

---

## 👤 Author

**Aman Shingane**
- GitHub: [@AmanShingane](https://github.com/AmanShingane)
