def build_profile(first, last, **user_info):
    """create a dictionary about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('yusuf', 'yassir',
                           location = 'sudan',
                           field = 'engineering')
print(my_profile)