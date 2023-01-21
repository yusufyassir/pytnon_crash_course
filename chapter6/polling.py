friends = ['ghalia', 'amro', 'yasmin', 'ahmed', 'majid', 'assel']

favorite_languages = {
    'amro' : 'arduino_c',
    'yasmin' : 'html',
    'ghalia' : 'c',
    'ahmed' : 'css',
}

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"{friend.title()} thank you for taking the poll.")
    else:
        print(f"{friend.title()} please take the poll.")