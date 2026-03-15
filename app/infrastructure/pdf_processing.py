import fitz  # PyMuPDF 


def detect_intro_pages(pdf_path: str) -> int:
    # Open the PDF file using the provided path
    doc = fitz.open(pdf_path)

    try:
        # Get the page label definitions from the PDF.
        # These labels define how pages are numbered (roman, decimal, etc.)
        labels = doc.get_page_labels()

        # If the PDF has no page label table,
        # we cannot detect introduction pages
        if not labels:
            return 0

        # Iterate over each label rule in the label table
        for label in labels:

            # We are looking for the rule where:
            # - the numbering style is "D" (decimal: 1,2,3...)
            # - the first displayed page number is 1
            # - the rule does not start at page index 0
            if (
                label.get("style") == "D"
                and label.get("firstpagenum") == 1
                and label.get("startpage", 0) > 0
            ):
                # startpage is the internal page index where
                # the main decimal numbering begins.
                # This corresponds to the number of intro pages.
                return label["startpage"]

        # If no matching rule is found,
        # assume there are no introduction pages
        return 0

    finally:
        # Always close the PDF document to free resources
        doc.close()


def iter_pages_with_labels(pdf_path: str):
    # Open the PDF document using the given file path
    doc = fitz.open(pdf_path)

    try:
        # Iterate over all pages in the document
        for page in doc:

            # Extract the text content of the page
            # "text" returns the plain text version of the page
            text = page.get_text("text")

            # If the page contains no text (e.g., only images),
            # ensure we return an empty string instead of None
            if not text:
                text = ""

            # Retrieve the page label (the number shown in the PDF viewer)
            # This could be roman numerals (i, ii, iii) or decimal numbers (1, 2, 3)
            label = page.get_label()

            # If the page has no label defined in the PDF,
            # create a fallback label using the internal page number
            if not label:
                # page.number starts at 0, so we add 1 to match normal page numbering
                label = str(page.number + 1)

            # Yield a tuple containing:
            # - the internal page index (starting at 0)
            # - the page label (what the user sees in the document)
            # - the extracted text of the page
            yield (page.number, label, text)

    finally:
        # Always close the document to release resources
        doc.close()
