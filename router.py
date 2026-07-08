"""
Business Rule Engine
--------------------
Applies routing rules to the extracted insurance claim data.
"""

INVESTIGATION_KEYWORDS = [
    "fraud",
    "inconsistent",
    "staged"
]


def route_claim(data, missing_fields):
    """
    Returns:
        route (str)
        reason (str)
    """


    if missing_fields:
        return (
            "Manual Review",
            "One or more mandatory fields are missing."
        )


    description = data.get("Description", "").lower()

    for word in INVESTIGATION_KEYWORDS:
        if word in description:
            return (
                "Investigation Flag",
                f"Description contains suspicious keyword '{word}'."
            )

    claim_type = data.get("Claim Type", "").lower()

    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Claim involves an injury."
        )


    damage = data.get("Estimated Damage", "0")

    try:
        damage = int(str(damage).replace(",", "").replace("₹", "").strip())

        if damage < 25000:
            return (
                "Fast-track",
                "Estimated damage is below ₹25,000."
            )

    except ValueError:
        pass

    return (
        "Standard Processing",
        "Claim requires normal processing."
    )