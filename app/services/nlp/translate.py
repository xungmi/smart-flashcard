from app.local_models.translate.opus_mt_en_vi import EnViTranslator


translator = EnViTranslator()  # Load 1 lần khi app khởi động


def translate_en_to_vi(text: str) -> str:
    return translator.translate_one(text)

def translate_batch(texts: list[str]) -> list[str]:
    return translator.translate(texts)