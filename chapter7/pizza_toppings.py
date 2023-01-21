promt = "\nplease enter the topping you would like "
promt += "\nenter 'quit' after you added all topings "

toppings = ""
while True:
    toppings = input(promt)
    if toppings == 'quit':
        break
    print(f"{toppings} is being added")