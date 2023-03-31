def cities(city, country, pop = ''):
    """formats city and country in string"""
    if pop:
        return (f"{city.title()}, {country.title()} population {pop}")
    else:
        return (f"{city.title()}, {country.title()}")