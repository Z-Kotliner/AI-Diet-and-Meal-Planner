from agents.diet_agent import DietAgent
from agents.inventory_agent import InventoryAgent
from models import InventoryInput
from models.ask_input import AskInput
from models.ask_output import AskOutput
from models.diet_input import DietInput


class ManagerAgent:
    @staticmethod
    async def run(ask_input: AskInput) -> AskOutput:
        # Call InventoryAgent to get inventory_output with usable_items
        inventory_input = InventoryInput(items=ask_input.items)
        inventory_output = await InventoryAgent().run(inventory_input)

        # Pass usable_items to DietAgent to get DietOutput object.
        diet_input = DietInput(items=inventory_output.usable_items, diet=ask_input.diet)
        diet_output = await DietAgent().run(diet_input)

        # Return structured JSON data containing all three outputs.
        ask_output = AskOutput(usable_items=inventory_output.usable_items,
                               diet_filtered=diet_output.compatible_items,
                               suggestions=diet_output.suggested_recipe_ideas)

        return ask_output
