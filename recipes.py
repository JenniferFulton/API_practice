import requests as req

#create a function that will search spoonacular recipes and print results
def recipes(food):
    print(f"Recipes for {food}:")
    resp = req.get("https://api.spoonacular.com/recipes/complexSearch?query=banana&apiKey=2df2ffb1f528442cae5578169a24ec0e")
    print(resp.text)

#get user input for recipe search
food = input('Search Recipes: ')

#call recipe function to get recipes user searched for
recipes(food)

