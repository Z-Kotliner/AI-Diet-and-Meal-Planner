from pydantic import BaseModel
from typing import List


class InventoryResponse(BaseModel):
    """ A pydantic model that represents cleaned ingredient list and a text message. """
    usable_items: List[str]
    message: str
