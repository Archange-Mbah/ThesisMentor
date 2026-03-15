import os
import uuid
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.infrastructure.pdf_processing import detect_intro_pages

router = APIRouter()

UPLOAD_DIR = os.path.join("app", "static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file.
    Returns a JSON containing:
    - doc_id: unique identifier
    - file_url: URL to display the PDF in the frontend
    """

    # 1️ Check that a file was provided
    if not file or not file.filename:
        return JSONResponse({"error": "No file provided"}, status_code=400)

    # 2️ Reject non-PDF files
    if file.content_type != "application/pdf":
        return JSONResponse({"error": "Only PDF files are allowed"}, status_code=400)

    try:
        # 3️ Generate a unique document ID and safe filename
        doc_id = uuid.uuid4().hex
        filename = f"{doc_id}.pdf"
        save_path = os.path.join(UPLOAD_DIR, filename)

        # 4️ Save the uploaded PDF
        contents = await file.read()
        with open(save_path, "wb") as f:
            f.write(contents)
        # Detect introduction pages
        intro_page_count = detect_intro_pages(save_path)

        # 5️ Return info for frontend
        return JSONResponse({ 
            "status": "ok",
            "doc_id": doc_id,
            "file_url": f"/static/uploads/{filename}",
            "intro_page_count": intro_page_count
            })
        

    except Exception as e:
        # 6️ Catch any unexpected errors
        return JSONResponse({"error": f"Failed to upload file: {str(e)}"}, status_code=500)