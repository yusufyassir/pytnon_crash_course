favorite_numbers = {
    'amro' : [3, 7, 0],
    'aseel' : [],
    'yasmin' : [6, 8, 2],
    'ghalia' : [7, 3, 9],
    'fitoon' : [3, 8, 10],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} favorite numbers are: ")
    for number in numbers:
            print(f"    {number}")