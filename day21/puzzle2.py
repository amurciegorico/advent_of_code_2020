#!/usr/bin/env python3

def get_isolated_ingredient(allergens_possible_ingredients):
    for allergen in allergens_possible_ingredients:
        if len(allergens_possible_ingredients[allergen]) == 1:
            ingredient = allergens_possible_ingredients[allergen].pop()
            del allergens_possible_ingredients[allergen]
            return allergen, ingredient


with open("./data/data1") as file:
    allergens_possible_ingredients = {}
    for line in file.readlines():
        split_line = line.split(' (contains ')
        ingredients = set(split_line[0].split(' '))
        for allergen in split_line[1][:-2].split(', '):
            allergens_possible_ingredients[allergen] = allergens_possible_ingredients[allergen].intersection(ingredients) if allergen in allergens_possible_ingredients else ingredients
    allergen_ingredients = {}
    while len(allergens_possible_ingredients) > 0:
        isolated_allergen, ingredient = get_isolated_ingredient(allergens_possible_ingredients)
        allergen_ingredients[isolated_allergen] = ingredient
        for allergen in allergens_possible_ingredients:
            if ingredient in allergens_possible_ingredients[allergen]:
                allergens_possible_ingredients[allergen].remove(ingredient)
    print(','.join([allergen_ingredients[allergen] for allergen in sorted(list(allergen_ingredients.keys()))]))
