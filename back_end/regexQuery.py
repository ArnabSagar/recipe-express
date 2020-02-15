import pymongo
import json
import pprint
import re


def searchRecipes():
    # connecting to the Atlas cluster
    client = pymongo.MongoClient("mongodb+srv://npysklyw:Maer1234@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

    # accessing recipe collection
    db = client.RecipeOther
    Recipes = db.Recipe

    hits = Recipes.find({"Ingredients":{'$regex':'/.*chicken.*/'}})

    for hit in hits:
        pprint.pprint(hit)


def searchRecipes
