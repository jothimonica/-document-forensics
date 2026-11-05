from app.ingestion.file_handler import get_file_info


file_path = "../test_documents/sample.pdf"

result = get_file_info(file_path)

print("\n========== DOCUMENT FORENSIC INFORMATION ==========\n")

print(f"File Name       : {result['file_name']}")
print(f"File Extension  : {result['file_extension']}")
print(f"File Size       : {result['file_size_bytes']} bytes")
print(f"SHA-256         : {result['sha256']}")

print("\n====================================================\n")