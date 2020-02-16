from flask import Blueprint, jsonify
from pprint import pprint
from flask_pymongo import PyMongo
from .db import mongo

main = Blueprint('main', __name__)

@main.route("/find_matches")
def find_matches():
    test = {"Ingredients" : ["chicken", "butter"]}
    ingredients = test["Ingredients"]
    Recipes = mongo.cx.RecipeOther.Recipe

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

    ### NEED to convert from the type of hits object to JSON! 
    return hits


@main.route("/read_one")
def read_one():
    one = mongo.cx.RecipeOther.Recipe.find_one()
    name = one['Name']
    img = one['imgURL']
    ing = one['Ingredients']
    dic = {'Name':name,'imgURL':img,'Ingredients':ing}
    return jsonify(dic)

@main.route("/")
def start():
    return "fuck you"
