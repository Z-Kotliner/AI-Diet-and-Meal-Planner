from pydantic import BaseModel
from typing import List

from models import PlannerResponse


class RecommenderResponse(BaseModel):
    """ A pydantic model that represents list of recipes plans. """
    recipes: List[PlannerResponse]
