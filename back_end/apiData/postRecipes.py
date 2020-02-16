import pymongo

# takes a list of dictionaries representing the recipes to insert into database
def postRecipeData(recipes):
    # connecting to the Atlas cluster
    client = pymongo.MongoClient("mongodb+srv://npysklyw:hackathon@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority")

    # accessing recipe collection
    db = client.RecipeOther
    Recipes = db.Recipe
    
    # insert the recipes into database
    result = Recipes.insert_many(recipes)
    print(result.inserted_ids)

# tested and above code works
def test():
    data1 = {'Name': 'Chicken Penne', 'Ingredients': ["Chicken breast", "Alfredo sauce", "penne", "garlic", "black pepper", "butter", "Parmesan"] }
    
    data2 = {'Name': 'Toast', 'Ingredients': ["Bread"] }

    recipes = [data1, data2]

    postRecipeData(recipes)

#test()
