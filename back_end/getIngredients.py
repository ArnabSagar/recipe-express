# get the list of all possible ingredients from the list of all recipes

recipeFile = open("recipes.txt", 'r')
recipes = recipeFile.readlines()
recipeFile.close()
Ingredients = set()

for i in range(0, len(recipes)):
    items = recipes[i].split(',')
    newItems = []
    for j in range(0, len(items)):
        newItems.append(items[j].strip(' ').strip('\n'))
    items = newItems[1:]
    for item in items:
        if(not (item is "" or item is "\n" or item is " ")):
            Ingredients.add(item)

ingredientsFile = open("ingredients.txt", 'w')
for ing in Ingredients:
    ingredientsFile.write(ing + "\n")
ingredientsFile.close()
