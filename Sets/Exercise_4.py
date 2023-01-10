# The food truck has separate menus for drinks and food

drinks = {'Water', 'Soda'}
foods = {'Pizza', 'Hot Dog', 'PB&J', 'Salad'}

foods.update(drinks)

print('Combined menu: ', drinks.union(foods))
