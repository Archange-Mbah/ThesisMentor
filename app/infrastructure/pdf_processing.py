import fitz  # PyMuPDF


def detect_intro_pages(pdf_path: str) -> int:
    """
    TODO (Student Task):
    Implement intro-page detection using the PDF page-label table.

    Goal:
    - Some theses use roman numerals (i, ii, iii, ...) for the introduction pages,
      and then restart numbering at "1" for the main content.
    - This function should return how many pages come _before_ the first page
      labeled "1" (decimal numbering).

    Steps:
    1) Open the PDF with PyMuPDF using the provided `pdf_path`.
    2) Read the page label definitions using `doc.get_page_labels()`.
    3) Find the label range where:
       - style == "D"  (decimal numbering)
       - firstpagenum == 1
       - startpage > 0
       This startpage indicates the number of intro pages.
    4) Return that number (or 0 if not found).
    5) Close the PDF (always).

    Expected result:
    - If the PDF has roman intro pages and main content starts at label "1" on
      page index 6, return 6.
    - If the PDF has no label table or no restart at "1", return 0.

    Where this method must be used (after you implement it):
    - In the upload endpoint:
        app/api/endpoints/documents.py  (POST /upload)
      Right AFTER saving the uploaded PDF to disk (after you have `save_path`),
      call:
        intro_page_count = detect_intro_pages(save_path)
      Then include `intro_page_count` in the JSON response returned to the frontend.

    Testing requirement (must do):
    - After implementing this, run the tests in:
        tests/test_pdf_processing.py
    - The tests expect a PDF file at the test path (fixture), e.g.:
        tests/test_docs/sample.pdf
      If it does not exist, you must add a small PDF there before running tests.
    """
    # TODO: implement
    raise NotImplementedError


def iter_pages_with_labels(pdf_path: str):
    """
    TODO (Student Task):
    Implement a generator that iterates through the PDF and yields
    (page_index, label, text) for each page.

    Goal:
    - We need page text for indexing (chunking + embeddings).
    - We also need the page "label" (roman/decimal/custom) so later the chat can
      cite sources like [p.i] or [p.12].

    Where this method will be used:
    - In the indexing function (e.g. build_faiss_index) located in:
        app/services/indexing_service.py
      It will loop over this generator to process pages one-by-one.

    Requirements:
    1) Open the PDF using: fitz.open(pdf_path)
    2) Loop over all pages in the document
    3) For each page:
       - Extract text with: page.get_text("text")
         (if empty, use "" as fallback)
       - Extract page label with: page.get_label()
         If label is missing/empty, fallback to: str(page.number + 1)
       - Yield a tuple:
         (page.number, label, text)
    Important:
    - Always close the PDF even if an error occurs (use try/finally).

    Done when:
    - Calling this function in a small test prints correct labels:
        for page_index, label, text in iter_pages_with_labels(path):
            print(page_index, label, len(text))

    Testing requirement (must do):
    - After implementing this, run:
        pytest tests/test_pdf_processing.py
    - If there is no PDF at the test path (fixture), e.g.:
        tests/test_docs/sample.pdf
      you must add one before running the tests.
    """
    # TODO: implement
    raise NotImplementedError
