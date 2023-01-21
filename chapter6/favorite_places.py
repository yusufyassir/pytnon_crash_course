favorite_places = {
    'amro' : ['maldivs', 'toti', 'mk nimer'],
    'aseel' : [],
    'yasmin' : ['sea', 'pool', 'rooftop',],
    'ghalia' : ['bed', 'cafe', 'winter streets'],
    'fitoon' : ['organic', 'park', 'ahmeds car'],
    'noran' : ['nile street', 'vintage tea room',],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite places are: ")
    for place in places:
            print(f"    {place}.")