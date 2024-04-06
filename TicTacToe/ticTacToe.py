from board import Board
from player import Player
from playingPieceO import playingPieceO
from playingpieceX import playingPieceX
from collections import deque


class TicTacToeGame:
    def __init__(self):
        self.players = deque()
        self.game_board = None

    def initialize_game(self):
        # Creating 2 Players
        cross_piece = playingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = playingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True
        while no_winner:
            # Take out the player whose turn it is and put the player back at the end of the list
            player_turn = self.players.popleft()

            # Get free spaces from the board
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            # Read user input
            print(f"Player: {player_turn.name} Enter row,column: ", end="")
            s = input()
            input_row, input_column = map(int, s.split(","))

            # Place the piece
            piece_added_successfully = self.game_board.add_piece(input_row, input_column, player_turn.playingPiece)
            if not piece_added_successfully:
                # Player cannot insert the piece into this cell; player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            # Check if there's a winner
            if self.is_there_winner(input_row, input_column, player_turn.playingPiece.pieceType):
                return player_turn.name

        return "tie"

    def is_there_winner(self, row, column, pieceType):
        size = self.game_board.size

        # Check row
        row_match = all(self.game_board.board[row][i] and self.game_board.board[row][i].pieceType == pieceType for i in range(size))

        # Check column
        column_match = all(self.game_board.board[i][column] and self.game_board.board[i][column].pieceType == pieceType for i in range(size))

        # Check diagonal
        diagonal_match = all(self.game_board.board[i][i] and self.game_board.board[i][i].pieceType == pieceType for i in range(size))

        # Check anti-diagonal
        anti_diagonal_match = all(self.game_board.board[i][size - 1 - i] and self.game_board.board[i][size - 1 - i].pieceType == pieceType for i in range(size))

        return row_match or column_match or diagonal_match or anti_diagonal_match


if __name__ == "__main__":
    # Create a TicTacToeGame instance
    game = TicTacToeGame()

    # Initialize the game
    game.initialize_game()

    # Start the game and print the winner
    winner = game.start_game()
    print(f"Winner is: {winner}")
