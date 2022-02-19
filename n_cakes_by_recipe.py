def cakes(recipe, available):
    # check how many cakes can you make for a given recipe
    # and the available ingredients
    return min([available[item]//recipe[item] if item in available else 0 for item in recipe])
   


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))