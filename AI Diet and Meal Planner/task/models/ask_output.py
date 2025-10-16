from pydantic import BaseModel
from typing import List


class AskOutput(BaseModel):
    """ A pydantic model that represents the ManagerAgent's response. """
    usable_items: List[str]
    diet_filtered: List[str]
    suggestions: List[str]
