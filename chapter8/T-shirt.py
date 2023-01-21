def make_shirt(size, message):
    """prints shirt size and message to be printed"""
    print(f"\nthe shirt size is: {size}.")
    print(f"and the message is: {message}.")

size = input("please enter you size: ")
message = input("what do want to print: ")

make_shirt(size, message)