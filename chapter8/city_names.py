def city_countruy(city, country):
    """neetly prints city and country"""
    string = f'"{city.title()}, {country.title()}"'
    print(string)

c = input("please enter city: ")
cc = input("please enter country: ")

city_countruy(c, cc)