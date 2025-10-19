from fastapi import FastAPI

from agents import PlannerAgent
from agents import DietAgent
from agents import InventoryAgent
from agents import ManagerAgent
from agents import MultiRecipeAgent
from config import run_server
from config import setup_logger
from models import InventoryInput, PlannerInput, InventoryResponse, DietResponse, PlannerResponse, AskOutput, \
    RecommenderResponse
from models import AskInput
from models import DietInput
from models import RecommenderInput

# Set up logger
logger = setup_logger("app", "DEBUG")

# Create a FastAPI instance app
app = FastAPI(title="AI Diet & Meal Planner")


# Root endpoint
@app.get("/", response_model=dict)
async def root():
    return {"message": "AI Diet and Meal Planner API is up and running!"}


# POST route that accepts InventoryInput object as request body
@app.post("/inventory/", response_model=InventoryResponse)
async def inventory_endpoint(items: InventoryInput):
    inventory_data = InventoryAgent().run(items)
    return inventory_data


# POST route that accepts DietInput object as request body
@app.post("/diet/", response_model=DietResponse)
async def diet_endpoint(diet_input: DietInput):
    diet_data = DietAgent().run(diet_input)
    return diet_data


# POST route that accepts PlannerInput object as request body
@app.post("/plan/", response_model=PlannerResponse)
async def planner_endpoint(planner_input: PlannerInput):
    logger.info("Received /plan request: base_recipe=%s,", planner_input.base_recipe)
    meal_recipe = await PlannerAgent().run(planner_input)
    logger.info("/plan response: recipe title=%s, ingredients=%s, steps=%s", meal_recipe.title, meal_recipe.ingredients,
                meal_recipe.steps)
    return meal_recipe


# POST route that accepts AskInput object as request body
@app.post("/ask/", response_model=AskOutput)
async def manager_endpoint(ask_input: AskInput):
    logger.info("Received /ask request: items=%s, diet=%s", ask_input.items, ask_input.diet)
    ask_output = await ManagerAgent.run(ask_input)
    logger.info("/ask response: suggestions=%s", ask_output.suggestions)
    return ask_output


# Recommend Endpoint POST route that accepts RecommenderInput object as request body
@app.post("/recommend/", response_model=RecommenderResponse)
async def recommend_endpoint(recommender_input: RecommenderInput):
    logger.info("Received /recommend request: items=%s, diet=%s recipe_count=%s", recommender_input.items,
                recommender_input.diet, recommender_input.recipe_count)
    recipe_data = await MultiRecipeAgent.run(recommender_input)
    logger.info("/recommend response: recipes returned=%s", recipe_data.recipes)
    return recipe_data


# Entry point to run the server
if __name__ == "__main__":
    run_server()
