from sentence_transformers import SentenceTransformer
from typing import List

# Tải mô hình khi module được import
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # Dim: 384

def encode_text(text: str) -> List[float]:
    """
    Encode một đoạn văn thành vector embedding.
    """
    embedding = model.encode(text, convert_to_numpy=True).tolist()
    return embedding