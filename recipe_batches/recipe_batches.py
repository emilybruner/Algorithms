#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  total_batches = 0

  for key in recipe.keys():
    #see if this key has a match in ingredients 
    if key not in ingredients:
      return 0
    
    batches = ingredients[key]//recipe[key]
    if batches == 0:
      return 0

    if not total_batches:
      total_batches = batches

    else:
      total_batches = min(batches, total_batches)

  return total_batches


  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))