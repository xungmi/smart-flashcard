from app.local_models.example.flan_t5_base import FlanT5ExampleGenerator

example_generator = FlanT5ExampleGenerator()

def create_example_sentence(word: str) -> str:
    return example_generator.generate_example_sentence(word)
