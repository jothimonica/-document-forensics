from pathlib import Path
import hashlib


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".tiff",
    ".bmp"
}


def validate_file(file_path: str) -> bool:
    """
    Check whether the file exists and has a supported extension.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    return True


def calculate_sha256(file_path: str) -> str:
    """
    Calculate SHA-256 hash of the document.
    """

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:
            chunk = file.read(8192)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def get_file_info(file_path: str) -> dict:
    """
    Return basic forensic information about the file.
    """

    path = Path(file_path)

    validate_file(file_path)

    return {
        "file_name": path.name,
        "file_extension": path.suffix.lower(),
        "file_size_bytes": path.stat().st_size,
        "sha256": calculate_sha256(file_path)
    }