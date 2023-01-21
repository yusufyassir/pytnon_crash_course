def sandwich(*ingriedents):
    """prints what the sandwich is maade of"""
    print("the sandwich will have: ")
    for i in ingriedents:
        print(f"-{i.title()}")

sandwich('olive', 'cheese')

