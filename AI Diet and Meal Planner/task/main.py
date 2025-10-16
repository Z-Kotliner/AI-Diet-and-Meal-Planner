from fastapi import FastAPI

from agents import PlannerAgent
from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from agents.manager_agent import ManagerAgent
from agents.recipe_agent import MultiRecipeAgent
from config import run_server
from models import InventoryInput, PlannerInput
from models.ask_input import AskInput
from models.diet_input import DietInput
from models.recommender_input import RecommenderInput

# Create a FastAPI instance app
app = FastAPI(title="AI Diet & Meal Planner")


# Root endpoint
@app.get("/", response_model=dict)
async def root():
    return {"message": "Success!"}


# POST route that accepts InventoryInput object as request body
@app.post("/inventory/")
async def inventory_endpoint(items: InventoryInput):
    inventory_data = InventoryAgent().run(items)
    return inventory_data


# POST route that accepts DietInput object as request body
@app.post("/diet/")
async def diet_endpoint(diet_input: DietInput):
    diet_data = DietAgent().run(diet_input)
    return diet_data


# POST route that accepts PlannerInput object as request body
@app.post("/plan/")
async def planner_endpoint(planner_input: PlannerInput):
    meal_recipe = await PlannerAgent().run(planner_input)
    return meal_recipe


# POST route that accepts AskInput object as request body
@app.post("/ask/")
async def manager_endpoint(ask_input: AskInput):
    ask_output = await ManagerAgent.run(ask_input)
    return ask_output


# Recommend Endpoint POST route that accepts RecommenderInput object as request body
@app.post("/recommend/")
async def recommend_endpoint(recommender_input: RecommenderInput):
    recipe_data = await MultiRecipeAgent.run(recommender_input)
    return recipe_data


# Entry point to run the server
if __name__ == "__main__":
    run_server()
