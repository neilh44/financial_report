from fastapi import APIRouter, UploadFile
from app.services.ocr_service import extract_text_with_coordinates
from app.services.extraction_service import extract_financial_data

router = APIRouter()

@router.post("/")
async def extract_data(file: UploadFile):
    """
    Endpoint to extract data from financial reports using LlamaOCR.
    """
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Use LlamaOCR to process the file
    ocr_data = extract_text_with_coordinates(file_path)

    # Extract financial data
    extracted_data = extract_financial_data(ocr_data)

    return {"data": extracted_data, "coordinates": ocr_data.get("coordinates", [])}
