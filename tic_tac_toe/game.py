
# from tic_tac_toe import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row)+' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| '+' |'.join(row)+' |')

    def availabe_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for i, spot in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = "X"  # starting letter
    while game.empty_squares():
        if letter == "O":
            square = o_player.ge_moves(game)
        else:
            x_player.get_moves(game)

        # define a functin to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a more to {square}")
                game.print_board()
                print(" ")  # an empty line
            if game.current_winner:
                if print_game:
                    print(letter+"win")
                return letter
            letter = "O" if letter == "X" else "X"
        if print_game:
            print("it\'s a tie")
