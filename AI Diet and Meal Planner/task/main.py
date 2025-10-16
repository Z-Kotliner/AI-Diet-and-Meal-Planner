from fastapi import FastAPI

from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from agents.manager_agent import ManagerAgent
from config import run_server
from models import InventoryInput
from models.ask_input import AskInput
from models.diet_input import DietInput

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


# POST route that accepts AskInput object as request body
@app.post("/ask/")
async def manager_endpoint(ask_input: AskInput):
    ask_output = await ManagerAgent.run(ask_input)
    return ask_output


# Entry point to run the server
if __name__ == "__main__":
    run_server()
