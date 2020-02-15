import pymongo
import random

uri = "mongodb+srv://npysklyw:hackthevalley@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

# access the atlas cluster
client = pymongo.MongoClient(uri)

# access the recipes from mongodb
recipesDatabase = client.Recipe  # NAMEOFRECIPEDATABASE
recipesCollection = recipesDatabase.Recipe

#creating databases and collections from mongodb for the users inputted ingrediants
userDatabase = client.userTemp
userCollection = userDatabase.userTemp

#creating cursors from the collections we imported
recipeCursor = recipesCollection.find()
userCursor = userCollection.find()

#creating a list to store the user ingredients for easy searching
listUser = []

#Creating the list and adding user ingredients too it
for ingredientsUser in userCursor:
    listUser.append(ingredientsUser["UserIngredient"])


#this function will take the cloud stored recipes, and compare them with intputted ingredients to show
#possible meals
def checkout(recipe, user):

    final_pantry = []

    #cycle through all recipes, check to see if they are compatible
    for recipes in recipe:
        #cycle then through all of the users ingredients
        for users in user:
            #cycle through all of the recipe ingredients checking to see if there is one match
            if users not in recipes["Ingredients"]:
                continue
            else:
                final_pantry.append(recipes["Name"])
    #this will ensure that the response received back by the function will always have at least 5 recipes
    #otherwise, cutout function will be run, and will create a mega set of solutions
    return final_pantry
