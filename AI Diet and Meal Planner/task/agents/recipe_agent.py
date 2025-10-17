from agents import ManagerAgent, PlannerAgent
from models import RecommenderResponse, PlannerInput
from models import AskInput
from models import RecommenderInput


class MultiRecipeAgent:
    """ MultiRecipeAgent acts as an orchestrator between ManagerAgent(ask/) and PlannerAgent(plan/) """

    @staticmethod
    async def run(recommender_input: RecommenderInput) -> RecommenderResponse:
        # Call ManagerAgent to get recipe name suggestions
        ask_input = AskInput(items=recommender_input.items, diet=recommender_input.diet)
        ask_output = await ManagerAgent().run(ask_input)

        # Extract recipe_count from input
        recipe_count = recommender_input.recipe_count

        # Extract the top n suggestions from the output where n is recipe_count
        suggestions = ask_output.suggestions[:recipe_count]

        # Create an empty list for holding the recipe list
        recipe_list = []

        # For each suggestion call PlannerAgent to get recipes
        for meal in suggestions:
            # Create a Planner input using recipe_count number of meal names
            planner_input = PlannerInput(base_recipe=meal)

            # Run planner to get recipe
            recipe = await PlannerAgent().run(meal_name=planner_input)

            # Add recipe to list
            recipe_list.append(recipe)

        # Create RecipeResponse object using the recipe list
        recommender_response = RecommenderResponse(recipes=recipe_list)

        return recommender_response
