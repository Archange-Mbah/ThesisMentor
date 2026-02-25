import os
import uuid
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    # 1) Check that a file was provided
    if not file or not file.filename:
        return JSONResponse({"error": "No file provided"}, status_code=400)
    # 2) Optional: reject non-PDF files
    if file.content_type != "application/pdf":
        return JSONResponse({"error": "Only PDF files are allowed"}, status_code=400)
    # 3) Create the uploads folder if it does not exist
    upload_dir = os.path.join("app", "static", "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    # 4) Create a unique ID and filename
    doc_id = uuid.uuid4().hex
    filename = f"{doc_id}.pdf"
    save_path = os.path.join(upload_dir, filename)

    # 5) Read the uploaded file bytes and save to disk
    contents = await file.read()
    with open(save_path, "wb") as f:
        f.write(contents)

    # 6) Return info so the frontend can load the file
    return {
        "status": "ok",
        "doc_id": doc_id,
        "file_url": f"/static/uploads/{filename}",
    }

    return
