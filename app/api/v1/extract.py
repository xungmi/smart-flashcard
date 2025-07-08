from fastapi import APIRouter, UploadFile, File, HTTPException
from app.local_models.ocr.tesseract import extract_text_from_image as tesseract


router = APIRouter(prefix="/v1/extract", tags=["extract"])


@router.post("/image", summary="Trích xuất văn bản từ ảnh")
async def extract_text_from_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Chỉ hỗ trợ ảnh JPEG hoặc PNG")

    try:
        image_bytes = await file.read()
        extracted_text = tesseract(image_bytes)


        return {
            "success": True,
            "text": extracted_text,
            "message": "OCR thành công"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi xử lý OCR: {str(e)}")