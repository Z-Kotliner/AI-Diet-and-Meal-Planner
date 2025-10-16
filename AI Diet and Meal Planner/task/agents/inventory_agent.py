from models import InventoryResponse, InventoryInput
from services import LLMClient


# Define the prompt
def create_prompt(items):
    prompt = f"""You are a kitchen assistant. Given the list of ingredients input by user:\n
         {items}\n
         Return a JSON object with:\n
         usable_items: an array of ingredients that are non-empty and suitable for cooking (remove blank or invalid entries),\n
         message: a short confirmation string.\n"
        Respond ONLY with valid JSON."""

    return prompt


class InventoryAgent:
    def __init__(self):
        self.llm = LLMClient()

    async def run(self, user_input: InventoryInput) -> InventoryResponse:
        prompt = create_prompt(user_input.items)
        response = self.clean_and_parse(prompt)
        return response

    def clean_and_parse(self, prompt: str) -> InventoryResponse:
        response = self.llm.call_model_json(prompt, InventoryResponse)
        validated_response = InventoryResponse.model_validate(response)
        return validated_response
