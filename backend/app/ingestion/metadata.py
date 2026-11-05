import pymupdf


def extract_pdf_metadata(file_path: str) -> dict:
    """
    Extract basic PDF metadata and document information.
    """

    document = pymupdf.open(file_path)

    metadata = document.metadata

    result = {
        "page_count": len(document),
        "metadata": metadata
    }

    document.close()

    return result