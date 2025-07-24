from agno import Agent, Ollama

llm = Ollama(model="llama3")

recipe_agent = Agent(llm, description="A helpful agent that generates delicious recipes based on user input.")

@recipe_agent.tool
def generate_recipe(ingredients: str, cuisine: str = "any", diet: str = "none"):
    """Generate a recipe using ingredients. Optional cuisine and diet preferences can be added."""
    return f"""
    Create a recipe using the following ingredients: {ingredients}.
    Cuisine preference: {cuisine}.
    Dietary restriction: {diet}.

    The recipe should include:
    - Title
    - Ingredients List
    - Step-by-step Instructions
    - Cooking Time
    """

if __name__ == "__main__":
    print("Welcome to the Pushp AI Recipe Creator!")
    user_ingredients = input("Enter the ingredients you have (comma-separated): ")
    cuisine = input("Cuisine preference (e.g., Italian, Indian, Mexican) or 'any': ")
    diet = input("Dietary restriction (e.g., vegan, gluten-free) or 'none': ")

    result = recipe_agent.run("generate_recipe", ingredients=user_ingredients, cuisine=cuisine, diet=diet)
    print("\n🍽️ Your Recipe:\n")
    print(result)
