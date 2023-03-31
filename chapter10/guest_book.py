#entering multiple guest

name = ''
with open('guests_book.txt', 'w') as file:
    print("enter out to exit or a name to continue")
    while name != 'out':
        name = input("please enter your name: ")
        if name != 'out':
            print(f"hello there {name}")
            file.write(f"{name.title()} has entered.\n")

