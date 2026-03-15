import os
from app.infrastructure.pdf_processing import iter_pages_with_labels


def build_document_index(pdf_path: str):
    """
    Build a basic document index from a PDF.

    This function:
    1. Iterates through all pages of the PDF
    2. Extracts page text and labels
    3. Stores them in a structured list
    """

    pages_data = []

    # Iterate through the PDF using our generator
    for page_index, label, text in iter_pages_with_labels(pdf_path):

        page_info = {
            "page_index": page_index,   # internal index (0-based)
            "label": label,             # visible page label (i, ii, 1, 2...)
            "text": text                # extracted text
        }

        pages_data.append(page_info)

    return pages_data