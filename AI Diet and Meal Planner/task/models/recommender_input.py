from typing import List
from pydantic import BaseModel


class RecommenderInput(BaseModel):
    """ A pydantic model that represents user input for recipe recommendation. """
    items: List[str]
    diet: str
    recipe_count: int
