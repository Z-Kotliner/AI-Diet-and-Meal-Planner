from pydantic import BaseModel
from typing import List


class DietResponse(BaseModel):
    """ A pydantic model that represents the compatible ingredient list and the suggested recipe list. """
    compatible_items: List[str]
    suggested_recipe_ideas: List[str]
