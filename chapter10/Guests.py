"""takes guest name and store it in file"""
name = input("please enter your name: ")
guests = 'guests.txt'
with open(guests, 'w') as file:
    file.write(name)