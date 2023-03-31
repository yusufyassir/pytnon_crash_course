import json
number = int(input("pleas eneter youfavourite number: "))
with open('fav_num.txt', 'w') as f:
    json.dump(number, f)