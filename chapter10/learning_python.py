with open('learning_python.txt') as file:
    #contents = file.read()
    #for line in file:
    #    print(line.strip())
    content = ''
    for line in file:
        content += line

print(content)