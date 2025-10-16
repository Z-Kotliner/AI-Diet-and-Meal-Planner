from pydantic import BaseModel
from typing import List


class InventoryInput(BaseModel):
    """ A pydantic model that represents user input which is list of ingredients. """
    items: List[str]
