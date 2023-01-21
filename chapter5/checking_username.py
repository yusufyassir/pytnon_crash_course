current_users = ['ahmed', 'yassin', 'yusuf', 'amro',  'assad', 'moe']
new_users = ['zain', 'jawad', 'omer', 'foor', 'amro']
for user in new_users:
    if user in current_users:
        print(f"{user.title()} is not available please enter a new name")
    else:
        print(f"{user.title()} is available")