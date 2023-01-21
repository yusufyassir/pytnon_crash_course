promt = "enter you age: "
age = ""
while True:
    age = input(promt)
    age = int(age)
    if age < 3:
        print("ticket is free.")
    elif age < 12:
        print("ticket is $10.")
    elif age > 12:
        print("ticket is $15.")