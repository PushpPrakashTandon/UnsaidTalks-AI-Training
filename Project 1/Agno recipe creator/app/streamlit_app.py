import streamlit as st
from recipe_creator import recipe_agent

st.title("🥘 AI Recipe Creator")

ingredients = st.text_input("Enter ingredients (comma-separated)")
cuisine = st.selectbox("Cuisine", ["any", "Indian", "Italian", "Chinese", "Mexican"])
diet = st.selectbox("Diet", ["none", "vegetarian", "vegan", "gluten-free"])

if st.button("Generate Recipe"):
    result = recipe_agent.run("generate_recipe", ingredients=ingredients, cuisine=cuisine, diet=diet)
    st.markdown(result)
