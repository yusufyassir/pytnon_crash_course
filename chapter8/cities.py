def describe_city(city, country = 'UK'):
    """prints a simple text about city"""
    print(f"{city.title()}, is in {country.title()}.")

city = input("enter city: ")
country = input("enter country: ")
describe_city(city)

city = input("enter city: ")
country = input("enter country: ")
describe_city(city)

city = input("enter city: ")
country = input("enter country: ")
describe_city(city, country)