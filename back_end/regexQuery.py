import pymongo
import json
import pprint


def searchRecipes(ingredients):
    # connecting to the Atlas cluster
    client = pymongo.MongoClient("mongodb+srv://npysklyw:hackathon@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

    # accessing recipe collection
    db = client.RecipeOther
    Recipes = db.Recipe

    # conditional calls depending on number of input ingredients
    if (len(ingredients) == 1):
        regex1 = "^.*" + ingredients[0]
        hits = Recipes.find({"Ingredients":{'$regex':regex1}})
    elif (len(ingredients) == 2):
        regex1 = "^.*" + ingredients[0]
        regex2 = "^.*" + ingredients[1] 
        hits = Recipes.find({"Ingredients":{'$regex':regex1}, "Ingredients":{'$regex':regex2}})
    else:
        regex1 = "^.*" + ingredients[0]
        regex2 = "^.*" + ingredients[1] 
        regex3 = "^.*" + ingredients[2]
        hits = Recipes.find({"Ingredients":{'$regex':regex1}, "Ingredients":{'$regex':regex2}, "Ingredients":{'$regex':regex3}})


    for hit in hits:
        pprint.pprint(hit)

searchRecipes(["chicken", "ground pepper", "herbs"])
