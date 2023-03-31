def read_file(file_name):
    try:
        with open(file_name) as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("file is not found")



files = ['cats.txt', 'dogs.txt']
for file in files:
    read_file(file)
