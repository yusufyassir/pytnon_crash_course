my_pizzas = ['meat', 'cheese', 'pepporini', 'bbq' ]
friends_pizzas = my_pizzas[:]
my_pizzas.append('chicken')
friends_pizzas.append('spicey')
print("my favorite pizzas are")
for pizza in my_pizzas:
    print(pizza)
print("my friends favorite pizzas are")
for pizza in friends_pizzas:
    print(pizza)