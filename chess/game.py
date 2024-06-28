from chess.ai import Ai
from chess.board import Board
from chess.player import Player
import pandas as pd


class Game:
    def __init__(self, player):
        self.player_number = player
        self.board = Board()
        self.moves = pd.DataFrame(columns=["white", "black"])
        self.ai = None if player == 2 else Ai(self.board)
        self.players = [Player("white"), Player("black")]
        self.current_turn = "white"

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def handle_square_selection(self, i, j):
        if self.board.handle_square_selection(i, j, self.current_turn):
            self.save_move(self.board.last_move)
            if self.player_number == 2:
                self.switch_turn()
            if self.player_number == 1:
                self.ai.play_random()

    def save_move(self, move):
        if self.current_turn == "white":
            self.moves.loc[len(self.moves)] = [str(move), None]
        else:
            self.moves.loc[len(self.moves) - 1, "black"] = str(move)
        self.moves.to_csv("chess.csv", sep=";")
        print(self.moves)
