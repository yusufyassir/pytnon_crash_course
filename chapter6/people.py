person = {
    'first_name' : 'fitoon',
    'last_name' : 'ahmed',
    'ages' : 19,
    'city' : 'jabra',
}

person2 = {
    'first_name' : 'yusuf',
    'last_name' : 'yassir',
    'ages' : 19,
    'city' : 'omdur',
}

person1 = {
    'first_name' : 'shihab',
    'last_name' : 'omer',
    'ages' : 20,
    'city' : 'omdur',
}

peoples = [person, person1, person2]

for people in peoples:
    full_name = f"{people['first_name']} {people['last_name']}"
    age = people['ages']
    city = people['city']
    print(f"{full_name.title()}:")
    print(f"\t age is: {age}")
    print(f"\t lives in: {city}\n")