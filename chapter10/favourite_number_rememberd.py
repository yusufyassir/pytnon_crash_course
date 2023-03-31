#check for faviourite number and prints it
import json
try:
    with open('fav_num.txt', 'r') as f:
        favn = json.load(f)
except FileNotFoundError:
    number = int(input("pleas eneter youfavourite number: "))
    with open('fav_num.txt', 'w') as f:
        json.dump(number, f)
        print(f"we will rember that your favourite number is {number}")
else:
    print(f"your favourite number is {favn}")