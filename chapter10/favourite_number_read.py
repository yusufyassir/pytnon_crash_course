import json
with open('fav_num.txt', 'r') as f:
    favn = json.load(f)
    print(f"your favourite number is : {favn}")