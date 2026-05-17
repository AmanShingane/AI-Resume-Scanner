skills_dict = {

    "Programming Languages": [
        "python", "java", "javascript", "typescript",
        "c", "cpp", "csharp", "ruby", "go",
        "rust", "kotlin", "swift", "scala",
        "r", "matlab", "perl", "php",
        "bash", "shell", "sql", "html", "css",
    ],

    "Machine Learning / AI": [
        "machine learning", "deep learning",
        "natural language processing",
        "computer vision",
        "reinforcement learning",
        "transfer learning",
        "neural network",
        "convolutional neural network",
        "recurrent neural network",
        "transformer", "bert", "gpt",
        "llm", "generative ai",
        "diffusion model",
        "random forest", "xgboost",
        "gradient boosting", "svm",
        "naive bayes",
        "logistic regression",
        "linear regression",
        "clustering", "pca",
        "feature engineering",
        "model evaluation",
        "hyperparameter tuning",
        "mlops",
        "data augmentation",
    ],

    "Data Science": [
        "pandas", "numpy", "scipy",
        "matplotlib", "seaborn", "plotly",
        "data analysis",
        "data visualization",
        "statistical analysis",
        "exploratory data analysis",
        "feature selection",
        "data cleaning",
        "data wrangling",
        "big data",
        "data pipeline",
        "etl",
        "time series",
        "forecasting",
        "a/b testing",
    ],

    "Frameworks & Libraries": [
        "tensorflow", "pytorch", "keras",
        "scikit-learn", "huggingface",
        "spacy", "nltk", "opencv",
        "fastapi", "flask", "django",
        "streamlit", "gradio",
        "langchain", "llamaindex",
        "react", "vue", "angular",
        "nodejs", "express", "spring",
    ],

    "Cloud & DevOps": [
        "amazon web services",
        "google cloud platform",
        "microsoft azure",
        "docker", "kubernetes",
        "ci/cd", "jenkins",
        "github actions",
        "terraform", "ansible",
        "linux", "unix",
        "git", "github", "gitlab",
        "serverless", "lambda",
        "ec2", "s3", "gcs",
        "bigquery",
    ],

    "Databases": [
        "mysql", "postgresql",
        "mongodb", "redis",
        "elasticsearch",
        "cassandra", "dynamodb",
        "sqlite", "oracle",
        "snowflake", "hadoop",
        "spark", "hive",
        "kafka", "airflow",
    ],

    "Soft Skills": [
        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "critical thinking",
        "project management",
        "agile",
        "scrum",
        "time management",
        "collaboration",
        "adaptability",
    ],
}


def extract_skills(text):

    found_skills = {}

    text = text.lower()

    for category, skills in skills_dict.items():

        matched_skills = []

        for skill in skills:

            if skill.lower() in text:
                matched_skills.append(skill)

        if matched_skills:
            found_skills[category] = matched_skills

    return found_skills