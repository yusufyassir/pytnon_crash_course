def read_file(file_name):
    """reads file contents"""
    try:
        with open(file_name) as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        pass

files = ['cats.txt', 'dogs.txt']
for file in files:
    read_file(file)
