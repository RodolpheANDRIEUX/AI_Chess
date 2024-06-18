from chess.board import Board
from chess.player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("white"), Player("black")]
        self.current_turn = "white"

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def make_move(self, move):
        if self.board.is_valid_move(move):
            self.board.move_piece(move)
            self.switch_turn()

    def handle_square_selection(self, i, j):
        if self.board.handle_square_selection(i, j, self.current_turn):
            self.switch_turn()
