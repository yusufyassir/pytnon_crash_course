pet1 = {
    'name' : 'garfield',
    'owner' : 'george',
}

pet2 = {
    'name' : 'tom',
    'owner' : 'jerry',
}

pets = [pet1, pet2]
for pet in pets:
    print(f"the pets name is: {pet['name'].title()}.")
    print(f"and the owner is: {pet['owner'].title()}.\n")