import random
from time import sleep

moves = ['Rock', 'Paper', 'Scissor']

pc_move = random.choice(moves)

user_move = input("What's your move? ")

user_move = user_move.capitalize()

while user_move not in moves:
    print(f"{user_move} is not a move :(")
    sleep(0.3)
    user_move = input("What's your move? ")
    user_move = user_move.capitalize()

if user_move in moves:
    print('Rock')
    sleep(0.9)
    print('Paper')
    sleep(0.9)
    print('Scissor')
    sleep(0.45)
    print('...')
    sleep(0.45)
    if user_move == pc_move:
        print("\nIt's a draw!\n")
    elif user_move == 'Scissor' and pc_move == 'Paper':
        print("\nYou've won!!!\n")
    elif user_move == 'Rock' and pc_move == 'Scissor':
        print("\nYou've won!!!\n")
    elif user_move == 'Paper' and pc_move == 'Rock':
        print("\nYou've won!!!\n")
    else:
        print("\nHa! You've lost! :(\n") 
    print(f"You chose {user_move} and the pc chose {pc_move}.")
else:
    print(f"{user_move} is not a move :(")