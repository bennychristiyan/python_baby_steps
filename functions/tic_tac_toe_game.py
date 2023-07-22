board = [" " for i in range (9)]
def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]}|"
    row2 = f"| {board[3]} | {board[4]} | {board[5]}|"
    row3 = f"| {board[6]} | {board[7]} | {board[8]}|"
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(symbol):
    if symbol == "X":
        number = 1
    elif symbol == "O":
        number = 2
    print(f"Your turn player {number}")
    choice = int(input("Enter your move (1-9): "))
    if board[choice-1] == " ":
        board[choice-1] = symbol
    else:
        print()
        print("That space is already taken")

def victory(symbol):
    if (board[0] == board[1] == board[2] == symbol) or \
       (board[3] == board[4] == board[5] == symbol) or \
       (board[6] == board[7] == board[8] == symbol) or \
       (board[0] == board[3] == board[6] == symbol) or \
       (board[1] == board[4] == board[7] == symbol) or \
       (board[2] == board[5] == board[8] == symbol) or \
       (board[0] == board[4] == board[8] == symbol) or \
       (board[2] == board[4] == board[6] == symbol):
        return True
    else:
        return False

def draw():
    if " " not in board:
        return True
    else:
        return False
    
while True:
    print_board()
    player_move("X")
    if victory("X"):
        print_board()
        print("Player 1 wins! Congratulations!")
        break
    elif draw():
        print_board()
        print("It is draw")
        break
    print_board()
    player_move("O")
    if victory("O"):
        print_board()
        print("Player 2 wins! Congratulations!")
        break

# output
"""

|   |   |  |
|   |   |  |
|   |   |  |

Your turn player 1
Enter your move (1-9): 1

| X |   |  |
|   |   |  |
|   |   |  |

Your turn player 2
Enter your move (1-9): 2

| X | O |  |
|   |   |  |
|   |   |  |

Your turn player 1
Enter your move (1-9): 3

| X | O | X|
|   |   |  |
|   |   |  |

Your turn player 2
Enter your move (1-9): 4

| X | O | X|
| O |   |  |
|   |   |  |

Your turn player 1
Enter your move (1-9): 5

| X | O | X|
| O | X |  |
|   |   |  |

Your turn player 2
Enter your move (1-9): 6

| X | O | X|
| O | X | O|
|   |   |  |

Your turn player 1
Enter your move (1-9): 7

| X | O | X|
| O | X | O|
| X |   |  |

Player 1 wins! Congratulations!

"""