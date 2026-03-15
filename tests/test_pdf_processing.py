from pathlib import Path

from app.infrastructure.pdf_processing import detect_intro_pages, iter_pages_with_labels


def test_iter_pages_with_labels_yields_pages():
    pdf_path = Path("tests/test_docs/sample.pdf")
    assert pdf_path.exists(), "Missing test fixture: tests/test_docs/sample.pdf"

    pages = list(iter_pages_with_labels(str(pdf_path)))

    assert len(pages) > 0, "Expected at least 1 page"
    page_index, label, text = pages[0]

    assert isinstance(page_index, int)
    assert isinstance(label, str)
    assert label != ""  # must have a label or fallback
    assert isinstance(text, str)


def test_detect_intro_pages_returns_non_negative_int():
    pdf_path = Path("tests/test_docs/sample.pdf")
    assert pdf_path.exists(), "Missing test fixture: tests/fixtures/sample.pdf"

    intro_pages = detect_intro_pages(str(pdf_path))

    assert isinstance(intro_pages, int)
    assert intro_pages >= 0


# How to run these tests:
# 1) Activate your virtual environment (example):
#       source .venv/bin/activate
# 2) Install pytest (if not installed):
#       pip install pytest
# 3) From the project root (folder containing app/ and tests/), run:
#       pytest
#    Or run only this file:
#       pytest tests/test_pdf_processing.py
#    Or run a single test by name:
#       pytest -k test_iter_pages_with_labels_yields_pages
#    If you want to see print() output:
#       pytest -s
#
# Note:
# - Ensure the fixture PDF exists at: tests/test_docs/sample.pdf
# - If you get "No module named 'app'", run pytest from the project root
#   and make sure app/__init__.py exists.
