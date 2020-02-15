# Rip a bunch of recipes from Edamame API to use
import requests
import json
import pprint
import time

# base parameters
BASE_URL = "https://api.edamam.com/search"
APP_ID = "e8650a6b"
APP_KEY = "3cf3080f0b821238dfb1cd90a2346546"

# get the keywords to use in api calls
keywordsFile = open("keywordsToRip.txt", 'r')
keywords = keywordsFile.readlines()
keywordsFile.close()

# prepare output file
outFile = open("recipes.txt", 'w')

# iterate through api calls
count = 0
for key in keywords:
    count += 1
    if(count % 4 == 0):
        time.sleep(45)
    FULL_URL = BASE_URL + "?q=" + key + "&app_id=" + APP_ID + "&app_key=" + APP_KEY
    response = requests.get(url=FULL_URL)
    if not response.ok:
        print("keyword: " + key + " resulted in failed request!")
        continue
    data = response.json()
    hits = data["hits"]
    for hit in hits:
        recipe = hit["recipe"]
        outFile.write(recipe['label'] + ", ")
        outFile.write(str(recipe['yield']) + ", ")
        outFile.write(str(recipe['calories']) + ", ")
        ingredients = recipe['ingredients']
        for i in range(0, len(ingredients) - 1):
            outFile.write(ingredients[i]['text'] + ", ")
        outFile.write(ingredients[-1]['text'] + "\n")
    #print(data["hits"])
    #pprint.pprint(data)
