import sys

from extractor import extract_text, extract_fields
from validator import validate_fields
from router import route_claim
from output import generate_output, save_output


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py <path_to_pdf_or_txt>")
        return

    file_path = sys.argv[1]

    try:
        print("\nReading document...\n")
        document = extract_text(file_path)
        print(document)

    except Exception as e:
        print(f"\nError reading document:\n{e}")
        return

    try:
        print("\nExtracting fields...\n")
        fields = extract_fields(document)
        print(fields)

    except Exception as e:
        print("\nUnable to extract fields using Gemini API.")
        print("Possible reasons:")
        print("- Internet connection unavailable")
        print("- Invalid API Key")
        print("- Gemini API quota exceeded")
        print("- Gemini servers are temporarily busy")
        print(f"\nError:\n{e}")
        return

    print("\nValidating...\n")
    missing_fields = validate_fields(fields)
    print("Missing Fields:", missing_fields)

    print("\nRouting...\n")
    route, reason = route_claim(fields, missing_fields)

    print("Route :", route)
    print("Reason:", reason)

    print("\nGenerating JSON Output...\n")

    result = generate_output(
        fields,
        missing_fields,
        route,
        reason
    )

    output_file = save_output(result, file_path)

    print(f"\nResult saved successfully!")
    print(f"Saved to: {output_file}")

    print(result)

    print("\nResult saved successfully!")
    print("Saved to outputs/result.json")


if __name__ == "__main__":
    main()