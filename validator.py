from typing import Dict, List


MANDATORY_FIELDS = [
    "Policy Number",
    "Policyholder Name",
    "Incident Date",
    "Incident Time",
    "Location",
    "Description",
    "Claimant",
    "Asset Type",
    "Asset ID",
    "Estimated Damage",
    "Claim Type",
    "Attachments",
    "Initial Estimate"
]


def validate_fields(data: Dict):

    missing_fields = []

    for field in MANDATORY_FIELDS:

        value = data.get(field, "")

        if value is None:
            missing_fields.append(field)

        elif str(value).strip() == "":
            missing_fields.append(field)

    return missing_fields