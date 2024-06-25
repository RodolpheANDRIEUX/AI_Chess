from chess.ai import Ai
from chess.board import Board
from chess.player import Player


class Game:
    def __init__(self, player):
        self.player_number = player
        self.board = Board()
        self.ai = None if player == 2 else Ai(self.board)
        self.players = [Player("white"), Player("black")]
        self.current_turn = "white"

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def handle_square_selection(self, i, j):
        if self.board.handle_square_selection(i, j, self.current_turn):
            if self.player_number == 2:
                self.switch_turn()
            if self.player_number == 1:
                self.ai.play_random()
