from models import PlannerInput
from models import PlannerResponse
from services import LLMClient


# Define the prompt to retrieve a recipe from LLM
def create_prompt(meal_idea):
    prompt = f"""You are a kitchen assistant. Given the a meal name (such as  'Vegan Stir Fry', 'Chicken Pasta bake', 'Easy chicken curry' or 'Sesame Grilled salmon' etc.) - {meal_idea} input by user:\n
         you will turn it in to a complete ready-to-follow recipe (step-by-step cooking instruction) in the form of JSON object.
         Return a JSON object should include:\n
         
            title: a text title of the recipe. \n
            ingredients: an array of ingredients that are necessary for cooking the given meal plan. \n
            steps: an array of steps where each step shows the method (how-to) of making the meal.\n 
         
         Each step in steps array should be a dictionary consisting of the following keys-values:\n
           step_number: an int representing the step number. \n"
           instruction: a string which tells what to do in that particular step.
           
        Respond ONLY with valid JSON."""

    return prompt


class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()

    async def run(self, meal_name: PlannerInput) -> PlannerResponse:
        prompt = create_prompt(meal_name.base_recipe)
        response = self.get_meal_recipe(prompt)
        return response

    def get_meal_recipe(self, prompt: str) -> PlannerResponse:
        response = self.llm.call_model_json(prompt, PlannerResponse)
        validate_response = PlannerResponse.model_validate(response)
        return validate_response
