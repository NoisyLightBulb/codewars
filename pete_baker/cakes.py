import math

def cakes(recipe, available):

    #iterate through recipe ingredients
    how_many_cakes = -1
    for ingredient in recipe:
        amount = recipe[ingredient]

        # print(f"{amount} of {ingredient}")

        #check resource availability
        if ingredient in available:
            #compute availability per ingredient
            number = math.floor(available[ingredient] / amount)

            if how_many_cakes == -1 or number < how_many_cakes:
                how_many_cakes = number


            # print(f"{number} times the amount of {ingredient} available")
        else:
            #at least one ingredient missing
            return 0

    return how_many_cakes



#TEST CASES
print(f'Cake 1: {cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})}')
# must return 2

print(f'Cake 2: {cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})}')
# must return 0
