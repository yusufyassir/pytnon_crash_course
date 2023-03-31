def count_words(file_name, wordd):
    """reads how many times a word has apeared"""
    try:
        with open(file_name, encoding='utf-8') as f:
         content = f.read()
    except FileNotFoundError:
        print("file not found")
    else:
        words = content.split()
        num = words.count(wordd)
        print(f"{wordd} has appered {num} times")

file_name = 'moby_dick.txt'
count_words(file_name, 'Moby')