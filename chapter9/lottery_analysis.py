from random import choices

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
my_ticket = [1, 'a', 3, 'f']
winner = choices(list, k=4)
attempts = 0

while (my_ticket != winner):
    winner = choices(list, k=4)
    #print(winner)
    attempts += 1

print(f"it took {attempts} attempts for you to win")