from models import DietInput
from models import DietResponse
from services import LLMClient


def create_prompt(items, diet):
    prompt = f"""You are a kitchen assistant. Given the list of ingredients input by user:\n
         {items}\n and diet type of {diet} (like Vegan, Keto, Mediterranean, Gluten-Free, or Paleo)
         Return a JSON object with:\n
         compatible_items: an array of ingredients selected from the given list of ingredients that are suitable for cooking the suggested_recipe_ideas ,\n
         suggested_recipe_ideas: an array of suggested recipe ideas that are friendly with the specified diet - {diet} and applies dietary rules that can be cooked using those ingredients..\n"
        Respond ONLY with valid JSON."""

    return prompt


class DietAgent:
    def __init__(self):
        self.llm = LLMClient()

    async def run(self, diet_input: DietInput) -> DietResponse:
        prompt = create_prompt(diet_input.items, diet_input.diet)
        response = self.get_suggested_recipe(prompt)
        return response

    def get_suggested_recipe(self, prompt: str) -> DietResponse:
        response = self.llm.call_model_json(prompt, DietResponse)
        validated_response = DietResponse.model_validate(response)
        return validated_response
