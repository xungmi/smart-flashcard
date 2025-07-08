from PIL import Image
import pytesseract
import io

def extract_text_from_image(image_bytes: bytes) -> str:
    # Load ảnh từ bytes (ảnh được gửi từ client)
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Dùng pytesseract để nhận dạng text
    text = pytesseract.image_to_string(image, lang='eng')

    return text.strip()
