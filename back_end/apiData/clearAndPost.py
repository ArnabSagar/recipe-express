import pymongo
import json
import postRecipes

# get a list of dictionaries representing the recipes
def readRecipes():
    recipeFile = open("recipes.txt", 'r')
    recipes = recipeFile.readlines()
    recipeList = []
    for recipe in recipes:
        items = recipe.split(',')
        name = items[0]
        ingredients = []
        for i in range(1, len(items)):
            ingredients.append(items[i].strip(' ').strip('\n'))
        recipeList.append({'Name': name, 'Ingredients': ingredients})
    return recipeList

def clearData(): 
    # connecting to the Atlas cluster
    client = pymongo.MongoClient("mongodb+srv://npysklyw:hackthevalley@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

    # accessing recipe collection
    db = client.RecipeOther
    Recipes = db.Recipe

    # remove all documents from the collection
    Recipes.remove({})

# clear the old mongodb collection and post the new data
def run():
    clearData()
    postRecipes.postRecipeData(readRecipes())


run()

