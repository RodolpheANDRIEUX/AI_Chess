import tkinter as tk

from chess.game import Game
from gui.board_view import BoardView


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.game = Game()
        self.board_view = BoardView(self, self.game)
