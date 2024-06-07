import tkinter as tk


class BoardView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.squares = None
        self.theme = ['#ebecd0', '#739552']
        self.create_widgets()

    def create_widgets(self):
        self.squares = {}
        # self.squares = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                square = Square(self.theme[(i + j) % 2])
                square.grid(row=i, column=j)
                self.squares[(i, j)] = square

    def update_board(self, board):
        for i in range(8):
            for j in range(8):
                piece = board.get_piece_at(i, j)
                if piece is not None:
                    self.squares[i][j].config(text=str(piece))
                else:
                    self.squares[i][j].config(text='')


class Square(tk.Canvas):
    def __init__(self, color, size=100):
        tk.Canvas.__init__(self, width=size, height=size, bg=color)
        self.size = size
        self.color = color
        self.bind('<Button-1>', self.click)
        self.piece = None

