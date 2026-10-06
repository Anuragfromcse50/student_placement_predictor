🎓 Student Placement Predictor

link - https://anuragfromcse50-student-placement-predictor-app-kiosgv.streamlit.app/

A machine-learning web application that predicts whether a student is
likely to be placed using academic and activity-related information.

Project Overview

Project: Student Placement Predictor

Type: Machine Learning / Classification

Frontend: Streamlit

ML: Python + scikit-learn

Model: Random Forest Classifier

Persistence: Joblib

Original API: Flask

Reported test score: 90.2%

Repository: student_placement_predictor

Developed as an AI/ML project for MLH × GDG Hack Day Prayagraj 2026
preparation.

Features

Placement prediction

Branch selection

CGPA input

Internship count

Project count

Random Forest prediction

Saved model and encoders

Streamlit web interface

Existing Flask REST API

GitHub and Streamlit Cloud deployment support

Input Features

Feature               Description

Branch              Engineering branch
CGPA                Student CGPA
No_of_Internships   Number of internships
No_of_Projects      Number of projects

Target:

Placed

Branches used in the dataset include:

ME
CSE
EE
ECE
CE
IT

Machine Learning Workflow

Load Dataset
     ↓
Explore Data
     ↓
Preprocess Data
     ↓
Encode Branch and Target
     ↓
Train-Test Split
     ↓
Train Random Forest
     ↓
Evaluate Model
     ↓
Create Prediction Function
     ↓
Save Model and Encoders

Preprocessing

LabelEncoder is used for:

Branch

Placed

The saved branch encoder must be used during prediction so that branch
encoding remains consistent with training.

Model

The model is:

RandomForestClassifier(random_state=42)

Train/test split:

train_test_split(
    test_size=0.2,
    random_state=42
)

Reported score:

90.2%

Reported confusion matrix:

[[261, 52],
 [46, 641]]

Example

Input:

Branch: CSE
CGPA: 8.5
Internships: 2
Projects: 3

Prediction:

Yes

Project Structure

student_placement_predictor/
│
├── app.py
├── placement.ipynb
├── placement.ui
├── placement_ui.py
├── main.py
├── requirements.txt
│
└── backend/
    ├── app.py
    ├── placement_model.pkl
    ├── branch_encoder.pkl
    ├── target_encoder.pkl
    └── student_placement_dataset_5000.csv

Files

app.py

Main Streamlit frontend. It collects student details, loads the saved
model and encoders, prepares the input, performs prediction, and
displays the result.

placement.ipynb

Jupyter Notebook containing the dataset processing, encoding, model
training, evaluation, prediction function, and model saving workflow.

backend/app.py

Original Flask REST API.

Endpoint:

POST /predict

Expected request:

{
  "branch": "CSE",
  "cgpa": 8.5,
  "internships": 2,
  "projects": 3
}

Example response:

{
  "prediction": "Yes"
}

Saved model files

placement_model.pkl
branch_encoder.pkl
target_encoder.pkl

requirements.txt

streamlit
pandas
joblib
scikit-learn

Run Streamlit Locally

cd "C:\Users\Hp\OneDrive\Desktop\HackDay_2026\student_placement_predictor"
streamlit run app.py

Open:

http://localhost:8501

Do not use python app.py for the Streamlit frontend.

Run Flask API

cd "C:\Users\Hp\OneDrive\Desktop\HackDay_2026\student_placement_predictor\backend"
python app.py

API address:

http://127.0.0.1:5000

Endpoint:

POST /predict

The Flask API expects:

{
  "branch": "CSE",
  "cgpa": 8.5,
  "internships": 2,
  "projects": 3
}

The backend converts these into the model feature names:

Branch
CGPA
No_of_Internships
No_of_Projects

Streamlit Cloud

Deployment settings:

Repository: Anuragfromcse50/student_placement_predictor
Branch: main
Main file: app.py

The root requirements.txt must contain all packages used by the
Streamlit application.

Git Workflow

git status
git add .
git commit -m "Update Student Placement Predictor"
git push

Security

Do not commit:

Virtual environments

Python cache files

Private credentials

Machine-specific secrets

Recommended .gitignore:

.venv/
.venv313/
__pycache__/
.ipynb_checkpoints/

Hackathon Value

This project demonstrates supervised learning, binary classification,
preprocessing, LabelEncoder, Random Forest, model evaluation, Joblib
model persistence, Flask REST API, Streamlit UI, Git/GitHub, and cloud
deployment.

Future Improvements

Prediction probability

More student features

Larger and better-balanced dataset

Algorithm comparison

Feature-importance charts

Personalized placement suggestions

Resume analysis

Skill-gap recommendations

Company-specific analytics

Placement trend visualization

Disclaimer

The prediction is a machine-learning estimate based on the training
data. It is not a guarantee of placement. Actual placement depends on
skills, interviews, communication, company requirements, market
conditions, and other factors.

Author

Anurag

Built as an AI/ML project for HackDay 2026 preparation.
