import json
import os


def generate_output(fields, missing_fields, route, reason):
    return {
        "extractedFields": fields,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reason
    }


def save_output(result, input_file):

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Get filename without extension
    filename = os.path.splitext(os.path.basename(input_file))[0]

    # Create JSON filename
    output_path = os.path.join("outputs", f"{filename}.json")

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    return output_path