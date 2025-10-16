from pydantic import BaseModel
from typing import List


class DietInput(BaseModel):
    """ A pydantic model that represents cleaned ingredient list and a Diet type. """
    items: List[str]
    diet: str
