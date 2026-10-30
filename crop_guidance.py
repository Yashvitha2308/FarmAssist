
"""
FarmAssist - Verified crop guidance

Source: ICAR-CRIDA, Agriculture Contingency Plan for Adilabad.
Document: 2011.
These are contingency suggestions, not universal crop recommendations.
"""

CROP_GUIDANCE = [
    {
        "state": "Telangana",
        "district": "Adilabad",
        "crop": "Maize",
        "season": "Contingency",
        "soil": ["Shallow black"],
        "water": "Irrigation required",
        "condition": (
            "Insufficient or delayed monsoon and lack of tank inflows"
        ),
        "reason": (
            "ICAR-CRIDA lists maize as an alternative irrigated crop "
            "for this specific situation."
        ),
        "source_name": "ICAR-CRIDA Adilabad Agriculture Contingency Plan",
        "source_year": 2011,
        "source_url": (
            "https://icar-crida.res.in/CP/Telangana/"
            "AP4-Adilabad%2031.1.2011.pdf"
        ),
        "verified": True
    },
    {
        "state": "Telangana",
        "district": "Adilabad",
        "crop": "Jowar",
        "season": "Contingency",
        "soil": ["Shallow black"],
        "water": "Irrigation required",
        "condition": (
            "Insufficient or delayed monsoon and lack of tank inflows"
        ),
        "reason": (
            "ICAR-CRIDA lists Jowar as an alternative irrigated crop "
            "for this specific situation."
        ),
        "source_name": "ICAR-CRIDA Adilabad Agriculture Contingency Plan",
        "source_year": 2011,
        "source_url": (
            "https://icar-crida.res.in/CP/Telangana/"
            "AP4-Adilabad%2031.1.2011.pdf"
        ),
        "verified": True
    }
]


def get_district_guidance(state, district, season=None):
    """Return verified records for a state and district."""
    matches = []

    for record in CROP_GUIDANCE:
        if not record.get("verified", False):
            continue

        if (
            record["state"].casefold() == state.casefold()
            and record["district"].casefold() == district.casefold()
        ):
            if season is None or record["season"].casefold() == season.casefold():
                matches.append(record)

    return matches


if __name__ == "__main__":
    results = get_district_guidance("Telangana", "Adilabad")

    print("Total verified records:", len(CROP_GUIDANCE))
    print("Adilabad guidance:")

    for record in results:
        print("-", record["crop"])
        print("  Condition:", record["condition"])
        print("  Source year:", record["source_year"])
