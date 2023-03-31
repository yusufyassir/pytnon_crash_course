usernames  = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("hello Admin would you like a status update")
        else:
            print(f"hello {user}, thank you for logging in ")
else:
    print("we need to find some users.py")