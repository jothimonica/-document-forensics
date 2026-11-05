from datetime import datetime


def parse_pdf_date(date_string: str):
    """
    Convert a PDF date such as:
    D:20261020171006+00'00'
    into a Python datetime.
    """

    if not date_string:
        return None

    try:
        clean_date = date_string.replace("D:", "")

        # Take only YYYYMMDDHHMMSS
        base_date = clean_date[:14]

        return datetime.strptime(
            base_date,
            "%Y%m%d%H%M%S"
        )

    except Exception:
        return None


def analyze_metadata(metadata: dict) -> list:
    """
    Analyze PDF metadata and generate forensic findings.
    """

    findings = []

    creation_date = parse_pdf_date(
        metadata.get("creationDate", "")
    )

    modification_date = parse_pdf_date(
        metadata.get("modDate", "")
    )

    # ----------------------------------------
    # CHECK 1: Creation date vs modification date
    # ----------------------------------------

    if creation_date and modification_date:

        if modification_date < creation_date:

            findings.append({
                "type": "METADATA_DATE_INCONSISTENCY",
                "severity": "MEDIUM",
                "observed": (
                    "Modification date is earlier than "
                    "creation date."
                ),
                "explanation": (
                    "The PDF metadata contains a temporal "
                    "inconsistency."
                )
            })

        else:

            findings.append({
                "type": "METADATA_DATE_CHECK",
                "severity": "NORMAL",
                "observed": (
                    "Modification date is equal to or later "
                    "than creation date."
                ),
                "explanation": (
                    "No basic creation/modification date "
                    "inconsistency was detected."
                )
            })

    # ----------------------------------------
    # CHECK 2: PDF encryption
    # ----------------------------------------

    encryption = metadata.get("encryption")

    if encryption and encryption.lower() != "none":

        findings.append({
            "type": "PDF_ENCRYPTION",
            "severity": "INFO",
            "observed": f"Encryption: {encryption}",
            "explanation": (
                "The PDF contains encryption information."
            )
        })

    else:

        findings.append({
            "type": "PDF_ENCRYPTION_CHECK",
            "severity": "NORMAL",
            "observed": "PDF is not encrypted.",
            "explanation": (
                "No PDF encryption was detected."
            )
        })

    return findings