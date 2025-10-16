from pydantic import BaseModel
from typing import List


class Step(BaseModel):
    """ A pydantic model that represents a single step in the cooking recipe with step number and instruction. """
    step_number: int
    instruction: str


class PlannerResponse(BaseModel):
    """ A pydantic model that represents a complete meal recipe with ingredients and  step-by-step instructions. """
    title: str
    ingredients: List[str]
    steps: List[Step]
