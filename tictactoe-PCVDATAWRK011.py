import os
import random


def display_board(board):
    print("\n" * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1, choose X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_maker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    a = random.randint(0, 1)
    if a == 0:
        return "player 1"
    else:
        return "player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("Welcome to Tic Tac Toe!")
while True:
    # reset board
    MyBoard = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first")

    start_game = input("Are you ready to play? Yes or No: ")

    if start_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "player 1":
            # Player 1s turn
            display_board(MyBoard)
            position = player_choice(MyBoard)
            place_maker(MyBoard, player1_marker, position)

            if win_check(MyBoard, player1_marker):
                display_board(MyBoard)
                print("Congratz" + turn)
                game_on = False
            else:
                if full_board_check(MyBoard):
                    display_board(MyBoard)
                    print("The game is a draw")
                    break
                else:
                    turn = "player 2"
        else:
            # Player 2s Turn
            display_board(MyBoard)
            position = player_choice(MyBoard)
            place_maker(MyBoard, player2_marker, position)

            if win_check(MyBoard, player2_marker):
                display_board(MyBoard)
                print("congratz" + turn)
                game_on = False
            else:
                if full_board_check(MyBoard):
                    display_board(MyBoard)
                    print("The game is a draw")
                    break
                else:
                    turn = "player 1"
    if not replay():
        break
