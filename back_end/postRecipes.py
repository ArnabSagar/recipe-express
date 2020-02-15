import pymongo

# takes a list of dictionaries representing the recipes to insert into database
def postRecipeData(recipes):
    #connecting to the Atlas database
    client = pymongo.MongoClient("mongodb+srv://npysklyw:Maer1234@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

    db = client.Recipe
    Recipes = db.Recipe

    result = Recipes.insert_many(recipes)
    print(result.inserted_ids)

