import os
import uuid
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    # 1) Check that a file was provided

    # 2) Optional: reject non-PDF files

    # 3) Create the uploads folder if it does not exist

    # 4) Create a unique ID and filename

    # 5) Read the uploaded file bytes and save to disk

    # 6) Return info so the frontend can load the file

    return
