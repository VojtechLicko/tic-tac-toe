import random

# How would i turn a normal program into OOP ?


class Player:
    def __init__(self) -> None:
        pass

    def move_player(self, player_char):
        player_turn = "not a digit"
        while not (str(player_turn).isdigit()) and player_turn not in range(1, 10):
            try:
                player_turn = int(
                    input(f"Player {player_char} enter your move (1-9) : ")
                )
            except ValueError:
                print("U have to enter a digit")
            if player_turn not in range(1, 10):
                print("The number hast to be in range 1-9")
        return player_turn, player_char


class Board:
    player_moves = []

    def __init__(self) -> None:
        pass

    def create_board(self):
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

    def update_board(self, board, move, player):
        board_places = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}
        board[board_places.get(move)] = player
        return board

    def print_board(self, board):
        print(100 * "\n")
        print("Current state of board is :")
        print(board[0] + "|" + board[1] + "|" + board[2])
        print("--------------------")
        print(board[3] + "|" + board[4] + "|" + board[5])
        print("--------------------")
        print(board[6] + "|" + board[7] + "|" + board[8])

    def check_win_conditions(self, board):
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

    def check_tie_condition(self, player_moves):
        if len(player_moves) == 9:
            return True
        return False


def play():
    keep_playing = True

    while keep_playing:
        if random.randint(0, 1) == 0:
            player_characters = ["   x   ", "   o   "]
        else:
            player_characters = ["   o   ", "   x   "]
        brd = Board()
        my_board = brd.create_board()
        p1 = Player()
        p2 = Player()

        while True:
            brd.print_board(my_board)
            player_moves = []
            turn_p1, p1_char = p1.move_player(player_characters[0])
            while turn_p1 in player_moves:
                while not (
                    (str(turn_p1).isdigit())
                    or turn_p1 not in range(1, 10)
                    or turn_p1 in player_moves
                ):
                    if turn_p1 not in range(1, 10):
                        print("The number hast to be in range 1-9")
                    if turn_p1 in player_moves:
                        print(
                            "This move has already been played,\
                        enter a new one"
                        )
                    try:
                        turn_p1 = int(
                            input(
                                f"Player {p1_char}\
                                enter your move(1-9) again: "
                            )
                        )
                    except ValueError:
                        print("U have to enter a digit")
            player_moves.append(turn_p1)
            my_board = brd.update_board(my_board, turn_p1, player_characters[0])
            brd.print_board(my_board)
            if brd.check_win_conditions(my_board):
                print(f"Player {player_characters[0]} won")
                break
            if brd.check_tie_condition(player_moves):
                print("Game over, Tie")
                break

            turn_p2, p1_char = p2.move_player(player_characters[1])
            while turn_p2 in player_moves:
                while (
                    not (str(turn_p2).isdigit())
                    or turn_p2 not in range(1, 10)
                    or turn_p2 in player_moves
                ):
                    if turn_p2 not in range(1, 10):
                        print("The number hast to be in range 1-9")
                    if turn_p2 in player_moves:
                        print(
                            "This move has already been played,\
                            enter a new one"
                        )
                    try:
                        turn_p2 = int(
                            input(
                                f"Player {player_characters[1]}\
                                enter your move(1-9) again: "
                            )
                        )
                    except ValueError:
                        print("U have to enter a digit")

            player_moves.append(turn_p2)
            my_board = brd.update_board(my_board, turn_p2, player_characters[1])
            brd.print_board(my_board)
            if brd.check_win_conditions(my_board):
                print(f"Player {player_characters[1]} won")
                break
            if brd.check_tie_condition(player_moves):
                print("Game over, Tie")
                break
        question = input("If you want to stop playing type (N)")
        if question == "N":
            keep_playing = False
        else:
            print(100 * "\n")


if __name__ == "__main__":
    play()
