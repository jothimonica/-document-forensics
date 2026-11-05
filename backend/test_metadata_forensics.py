from app.ingestion.metadata import extract_pdf_metadata
from app.forensics.metadata_forensics import analyze_metadata


file_path = "../test_documents/sample.pdf"

metadata_result = extract_pdf_metadata(file_path)

findings = analyze_metadata(
    metadata_result["metadata"]
)

print("\n========== METADATA FORENSIC ANALYSIS ==========\n")

for finding in findings:

    print(f"Type       : {finding['type']}")
    print(f"Severity   : {finding['severity']}")
    print(f"Observed   : {finding['observed']}")
    print(f"Explanation: {finding['explanation']}")
    print("-----------------------------------------------")

print("\n================================================\n")