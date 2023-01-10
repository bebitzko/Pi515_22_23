# Create your order for the food truck and see if your order is available

menu = {'Pizza', 'Hot Dog', 'PB&J', 'Salad', 'Water', 'Soda'}

my_order = {'Pizza', 'Hot Dog', 'Salad', 'Water', 'Soda'}

print('Order Available: ', set([]).issubset(menu))

# Make an order that isn't available

my_dream_order = {'Ice Cream', 'Fries', 'Falafel', 'Filet Mignon', 'Garlic Coca Cola', 'Orange Fanta Pop Tarts', 'Tab Clear'}

print('Order not Available: ', menu.issuperset(my_dream_order))
