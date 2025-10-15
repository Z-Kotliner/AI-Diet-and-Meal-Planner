from fastapi import FastAPI
from config import run_server

# Create a FastAPI instance app that defines routes and handles requests
app = FastAPI(title="AI Diet & Meal Planner")


# Root endpoint
@app.get("/", response_model=dict)
async def root():
    return {"message": "Success!"}


# Entry point to run the server
if __name__ == "__main__":
    run_server()
