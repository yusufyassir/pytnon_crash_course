print("enter numbers to add\n and q to quit")
num1 = 0
while num1 != 'q':
    try:
        num1 = int(input("enter first number: "))
        num2 = int(input("enter seconed number"))
    except ValueError:
        print("stings are not numbers")
    else:
        print(f"{num1} + {num2} = {num1+num2}")