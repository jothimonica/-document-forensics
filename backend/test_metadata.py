from app.ingestion.metadata import extract_pdf_metadata


file_path = "../test_documents/sample.pdf"

result = extract_pdf_metadata(file_path)

print("\n========== PDF FORENSIC METADATA ==========\n")

print(f"Page Count   : {result['page_count']}")

print("\nMetadata:")

for key, value in result["metadata"].items():
    print(f"{key}: {value}")

print("\n===========================================\n")