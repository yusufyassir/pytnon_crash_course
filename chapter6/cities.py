cities = {
    'london' : {
        'country' : 'united kingdom',
        'population' : 9000000,
    },
    'new york': {
        'country': 'USA',
        'population': 8648000,
    },
    'khartoum': {
        'country': 'sudan',
        'population': 5274321,
    },
}

for city_name, city_info in cities.items():
    print(f"\n{city_name.title()}:")
    print(f"\tis in {city_info['country'].title()}")
    print(f"\tand has a population of: {city_info['population']}")