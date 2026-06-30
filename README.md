# Candidate Data Transformation Pipeline

## Overview

The Candidate Data Transformation Pipeline is a Flask-based web application that transforms candidate information from multiple data sources into a standardized canonical profile. The application parses recruiter CSV and GitHub JSON files, normalizes candidate information, merges records, calculates confidence scores, tracks provenance, and exports the transformed profiles as a JSON file.

---

## Features

- Recruiter CSV Parsing
- GitHub JSON Parsing
- Candidate Data Normalization
- Candidate Profile Merging
- Duplicate Skill Removal
- Confidence Score Calculation
- Provenance Tracking
- Canonical JSON Generation
- Interactive Flask Dashboard

---

## Technologies Used

- Python 3.x
- Flask
- Pandas
- HTML
- CSS
- JSON

---

## Project Structure

```
candidate-data-transformation-pipeline/
│
├── app.py
├── requirements.txt
├── README.md
├── Technical_Design.pdf
├── pipeline/
│   ├── parsers/
│   ├── processors/
│   └── utils/
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── style.css
│   ├── background.jpg
│   └── logo.png
├── data/
│   ├── input/
│   └── output/
└── tests/
```

---

# Installation & Execution

## Step 1: Clone the Repository

```bash
git clone https://github.com/Snithya02/candidate-data-transformation-pipeline.git
```

## Step 2: Navigate to the Project Folder

```bash
cd candidate-data-transformation-pipeline
```

## Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python app.py
```

## Step 5: Open the Browser

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

## Step 6: Upload Input Files

Upload the following files:

- Recruiter CSV File
- GitHub JSON File

Click **Transform** to process the candidate data.

## Step 7: View Results

The application displays:

- Candidate Dashboard
- Candidate Profiles
- Confidence Scores
- Pipeline Status
- Output File Information

---

# Produced Output

After successful execution, the application generates:

```
data/output/final_candidates.json
```

The output contains the following standardized fields:

- Candidate ID
- Full Name
- Email
- Phone Number
- Current Company
- Job Title
- Skills
- Location
- GitHub Name
- Bio
- Links
- Experience
- Education
- Provenance
- Confidence Score

The transformed candidate information is also displayed through the Flask dashboard.

---

# Test Scenarios

The application was tested with the following scenarios:

| Test Case | Status |
|-----------|--------|
| Valid Recruiter CSV Upload | ✅ Passed |
| Valid GitHub JSON Upload | ✅ Passed |
| CSV Parsing | ✅ Passed |
| JSON Parsing | ✅ Passed |
| Candidate Data Normalization | ✅ Passed |
| Name Normalization | ✅ Passed |
| Email Normalization | ✅ Passed |
| Phone Number Normalization | ✅ Passed |
| Skill Normalization | ✅ Passed |
| Candidate Profile Merging | ✅ Passed |
| Duplicate Skill Removal | ✅ Passed |
| Confidence Score Calculation | ✅ Passed |
| Provenance Generation | ✅ Passed |
| Canonical JSON Export | ✅ Passed |
| Missing Values Handling | ✅ Passed |
| Flask Dashboard Rendering | ✅ Passed |

---

# Edge Cases Handled

- Missing email addresses
- Missing phone numbers
- Missing company or title
- Missing location
- Duplicate skills
- Different skill capitalizations
- Missing GitHub profile information
- Incomplete candidate profiles
- Missing values displayed as **N/A**

---

# Future Enhancements

- LinkedIn Profile Integration
- Resume PDF Parsing
- Automatic Experience Extraction
- REST API Support
- Database Integration
- AI-based Candidate Ranking
- Configurable Confidence Score Weights

---

# Author

**Nithya Shree S**

Bachelor of Engineering (Computer Science)

GitHub: https://github.com/Snithya02

---

# License

This project is developed for educational and assessment purposes as part of the **Eightfold Engineering Intern (Jul–Dec 2026) Assignment**.