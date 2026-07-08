# Autonomous Insurance Claims Processing Agent

## Overview

This project implements an Autonomous Insurance Claims Processing Agent that processes First Notice of Loss (FNOL) documents in PDF and TXT formats.

The application extracts important insurance claim information using Google's Gemini AI, validates mandatory fields, applies predefined business routing rules, and generates structured JSON output for downstream claim processing.

---

## Objective

The objective of this project is to automate the initial processing of First Notice of Loss (FNOL) documents by extracting key insurance claim information, validating mandatory fields, applying predefined routing rules, and generating structured JSON output for downstream claim processing.

---

## Features

- Supports PDF and TXT FNOL documents
- AI-powered field extraction using Google Gemini
- Detects missing mandatory fields
- Applies claim routing business rules
- Generates structured JSON output
- Modular Python architecture

---

## Architecture Diagram

                    +------------------------+
                    |     User / Evaluator   |
                    +-----------+------------+
                                |
                                | Upload PDF / TXT
                                v
                    +------------------------+
                    |       main.py          |
                    |  (Application Entry)   |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    |     extractor.py       |
                    |------------------------|
                    | • Read TXT             |
                    | • Read PDF             |
                    | • Extract Text         |
                    | • Gemini AI Extraction |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    |     validator.py       |
                    |------------------------|
                    | Check Mandatory Fields |
                    | Identify Missing Data  |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    |      router.py         |
                    |------------------------|
                    | Apply Business Rules   |
                    | • Fast-track           |
                    | • Manual Review        |
                    | • Investigation Flag   |
                    | • Specialist Queue     |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    |      output.py         |
                    |------------------------|
                    | Generate JSON Output   |
                    | Save to outputs/       |
                    +-----------+------------+
                                |
                                v
                    +------------------------+
                    |    fnolX.json Output   |
                    +------------------------+

---

## Project Structure

```
Autonomous Insurance Claims Processing Agent/
│
├── sample_documents/
│   ├── fnol1.txt
│   ├── fnol2.txt
│   ├── fnol3.txt
│   ├── fnol4.txt
│   └── fnol5.pdf
│
├── outputs/
│
├── config.py
├── prompts.py
├── extractor.py
├── validator.py
├── router.py
├── output.py
├── main.py
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## Approach

The application follows a modular pipeline:

1. Read the FNOL document (PDF/TXT)
2. Extract document text
3. Use Gemini AI to extract required fields
4. Validate mandatory fields
5. Apply business routing rules
6. Generate JSON output

---

## Routing Rules

| Condition | Route |
|-----------|-------|
| Estimated Damage < ₹25,000 | Fast-track |
| Missing mandatory fields | Manual Review |
| Description contains "fraud", "inconsistent", or "staged" | Investigation Flag |
| Claim Type = Injury | Specialist Queue |
| Otherwise | Standard Processing |

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project

```bash
cd "Autonomous Insurance Claims Processing Agent"
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Project

TXT

```bash
python main.py sample_documents/fnol1.txt
```

PDF

```bash
python main.py sample_documents/fnol5.pdf
```

---

## Output

The generated JSON file is saved inside the **outputs** folder.

Example:

```
outputs/
├── fnol1.json
├── fnol2.json
├── fnol3.json
├── fnol4.json
└── fnol5.json
```

---

## Technologies Used

- Python 3.12
- Google Gemini API
- pdfplumber
- python-dotenv

---

