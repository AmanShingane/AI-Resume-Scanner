import streamlit as st
import tempfile
import os
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

from src.parser import extract_text_from_pdf
from src.preprocess import preprocess_text
from src.vectorizer import get_embedding
from src.matcher import calculate_similarity
from src.skill_extractor import extract_skills

st.title("AI-Based Resume Screening System")

job_description = st.text_area(
    "Enter Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Screen Resumes"):

    if uploaded_files and job_description:

        jd_processed = preprocess_text(job_description)

        jd_embedding = get_embedding(jd_processed)

        results = []

        for uploaded_file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp_file:

                tmp_file.write(uploaded_file.read())

                tmp_path = tmp_file.name

            resume_text = extract_text_from_pdf(tmp_path)

            processed_resume = preprocess_text(resume_text)

            resume_embedding = get_embedding(processed_resume)

            score = calculate_similarity(
                resume_embedding,
                jd_embedding
            )

            skills = extract_skills(resume_text)

            results.append({
                "Resume": uploaded_file.name,
                "Match Score": score,
                "Skills": ", ".join(skills)
            })

            os.remove(tmp_path)

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Match Score",
            ascending=False
        )

        st.dataframe(df)

    else:
        st.warning("Upload resumes and enter job description.")