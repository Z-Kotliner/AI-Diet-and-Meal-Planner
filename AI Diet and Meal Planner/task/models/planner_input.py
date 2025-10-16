from pydantic import BaseModel


class PlannerInput(BaseModel):
    """ A pydantic model that represents a meal name(Base recipe) to be used by the planner agent. """
    base_recipe: str
