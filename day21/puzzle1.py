#!/usr/bin/env python3

with open("./data/data1") as file:
    allergens_ingredients = {}
    all_ingredients = []
    for line in file.readlines():
        split_line = line.split(' (contains ')
        ingredients = set(split_line[0].split(' '))
        for ingredient in ingredients:
            all_ingredients.append(ingredient)
        for allergen in split_line[1][:-2].split(', '):
            allergens_ingredients[allergen] = allergens_ingredients[allergen].intersection(ingredients) if allergen in allergens_ingredients else ingredients
    for ingredients in allergens_ingredients.values():
        for ingredient in ingredients:
            while ingredient in all_ingredients:
                all_ingredients.remove(ingredient)
    print(len(all_ingredients))
