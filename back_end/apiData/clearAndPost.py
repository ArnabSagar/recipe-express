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
        img = items[1]
        yiel = items[2]
        cals = items[3]
        ingredients = []
        for i in range(4, len(items)):
            ingredients.append(items[i].strip(' ').strip('\n'))
        recipeList.append({'Name': name, 'imgURL': img, 'yield': yiel, 'calories': cals, 'Ingredients': ingredients})
    return recipeList

def clearData(): 
    # connecting to the Atlas cluster
    client = pymongo.MongoClient("mongodb+srv://npysklyw:hackathon@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

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

