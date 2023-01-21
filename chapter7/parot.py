promt = "\ntell me something, and i will repeat it back to you: "
promt += "\nEnter 'quit' to end program. "

message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message.title())