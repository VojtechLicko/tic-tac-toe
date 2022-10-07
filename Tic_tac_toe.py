import random


def create_board():
    board = [
        "   7   ",
        "   8   ",
        "   9   ",
        "   4   ",
        "   5   ",
        "   6   ",
        "   1   ",
        "   2   ",
        "   3   ",
    ]
    return board


def move_player(player_char):
    player_turn = "not a digit"
    while not (str(player_turn).isdigit()) and player_turn not in range(1, 10):
        try:
            player_turn = int(input(f"Player {player_char} enter your move (1-9) : "))
        except ValueError:
            print("U have to enter a digit")
        if player_turn not in range(1, 10):
            print("The number hast to be in range 1-9")
    return player_turn, player_char


def update_board(board, move, player):
    board_places = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}
    board[board_places.get(move)] = player
    return board


def print_board(board):
    print(100 * "\n")
    print("Current state of board is :")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("--------------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("--------------------")
    print(board[6] + "|" + board[7] + "|" + board[8])


def check_conditions(board):
    return (
        (board[0] == board[1] == board[2])
        or (board[3] == board[4] == board[5])
        or (board[6] == board[7] == board[8])
        or (board[0] == board[4] == board[8])
        or (board[2] == board[4] == board[6])
        or (board[0] == board[3] == board[6])
        or (board[1] == board[4] == board[7])
        or (board[2] == board[5] == board[8])
    )


def play():
    if random.randint(0, 1) == 0:
        player_characters = ["   x   ", "   o   "]
    else:
        player_characters = ["   o   ", "   x   "]
    current_board = create_board()
    keep_playing = True
    while keep_playing:
        print("Current state of board is :")
        print(current_board[0] + "|" + current_board[1] + "|" + current_board[2])
        print("--------------------")
        print(current_board[3] + "|" + current_board[4] + "|" + current_board[5])
        print("--------------------")
        print(current_board[6] + "|" + current_board[7] + "|" + current_board[8])
        player_moves = []
        while True:
            if len(player_moves) == 9:
                print("Game over, Tie")
                break
            turn, player_1 = move_player(player_characters[0])
            while turn in player_moves:
                while not (
                    (str(turn).isdigit())
                    or turn not in range(1, 10)
                    or turn in player_moves
                ):
                    if turn not in range(1, 10):
                        print("The number hast to be in range 1-9")
                    if turn in player_moves:
                        print(
                            "This move has already been played,\
                        enter a new one"
                        )
                    try:
                        turn = int(
                            input(
                                f"Player {player_characters[0]}\
                                enter your move(1-9) again: "
                            )
                        )
                    except ValueError:
                        print("U have to enter a digit")
            player_moves.append(turn)
            current_board = update_board(current_board, turn, player_1)
            print_board(current_board)
            if check_conditions(current_board):
                print(f"player {player_characters[0]}  won")
                break
            if len(player_moves) == 9:
                print("Game over, Tie")
                break
            turn, player_2 = move_player(player_characters[1])
            while turn in player_moves:
                while not (
                    (str(turn).isdigit())
                    or turn not in range(1, 10)
                    or turn in player_moves
                ):
                    if turn not in range(1, 10):
                        print("The number hast to be in range 1-9")
                    if turn in player_moves:
                        print(
                            "This move has already been played,\
                             enter a new one"
                        )
                    try:
                        turn = int(
                            input(
                                f"Player {player_characters[1]}\
                                 enter your move (1-9) again : "
                            )
                        )
                    except ValueError:
                        print("U have to enter a digit")
            player_moves.append(turn)
            current_board = update_board(current_board, turn, player_2)
            print_board(current_board)
            if check_conditions(current_board):
                print(f"player {player_characters[1]}  won")
                break
        question = input("If you want to stop playing type (N)")
        if question == "N":
            keep_playing = False
        else:
            player_moves = []
            current_board = create_board()
            print(100 * "\n")


if __name__ == "__main__":
    play()
