import json
import pdfplumber
import time

from config import client
from prompts import EXTRACTION_PROMPT


def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_text(file_path):

    if file_path.lower().endswith(".pdf"):
        return read_pdf(file_path)

    elif file_path.lower().endswith(".txt"):
        return read_txt(file_path)

    else:
        raise ValueError("Unsupported file type.")



def extract_fields(document_text):

    prompt = EXTRACTION_PROMPT.format(
        document=document_text
    )

    for attempt in range(3):
        try:
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
            break
        except Exception as e:
            if attempt == 2:
                raise e

            print("Gemini is busy. Retrying in 5 seconds...")
            time.sleep(5)

    result = response.text.strip()


    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        data = json.loads(result)

    except json.JSONDecodeError:
        raise Exception(
            "Gemini returned invalid JSON.\n\n" + result
        )

    return data