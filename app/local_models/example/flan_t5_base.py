# app/local_models/example_model.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class FlanT5ExampleGenerator:
    def __init__(self, model_name="google/flan-t5-base", device=None):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        if device:
            self.device = torch.device(device)
        else:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model.to(self.device)

    def generate_example_sentence(self, word: str, temperature: float = 0.7, max_length: int = 64) -> str:
        prompt = f"Give an example sentence using the word '{word}'."
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        outputs = self.model.generate(
            **inputs,
            do_sample=True,
            temperature=temperature,
            max_length=max_length,
            top_k=50,
            top_p=0.95
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
