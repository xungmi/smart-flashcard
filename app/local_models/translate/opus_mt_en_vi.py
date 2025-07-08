from transformers import MarianMTModel, MarianTokenizer
import torch

class EnViTranslator:
    def __init__(self, device: str = None):
        model_name = "Helsinki-NLP/opus-mt-en-vi"
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

        # Chọn thiết bị: GPU nếu có, không thì CPU
        if device:
            self.device = device
        else:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = self.model.to(self.device)

    def translate(self, texts: list[str]) -> list[str]:
        """
        Dịch danh sách câu tiếng Anh sang tiếng Việt.
        :param texts: list[str] - danh sách câu tiếng Anh
        :return: list[str] - danh sách câu dịch tiếng Việt
        """
        encoded = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
        encoded = {key: val.to(self.device) for key, val in encoded.items()}

        with torch.no_grad():
            generated_tokens = self.model.generate(**encoded, max_length=128)

        translations = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return translations

    def translate_one(self, text: str) -> str:
        return self.translate([text])[0]
