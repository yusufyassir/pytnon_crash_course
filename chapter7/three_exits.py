promt = "enter you age: "
age = ""
active = True
while active:
    age = input(promt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("ticket is free.")
        elif age < 12:
            print("ticket is $10.")
        elif age > 12:
            print("ticket is $15.")
