import tkinter as tk


def darken_color(color):
    hex_color = color.lstrip('#')
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    darkened_rgb = tuple(max(0, int(c * 0.8)) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*darkened_rgb)


class ChessBoard:
    def __init__(self, root, width=100, height=100):
        self.squares = None
        self.root = root
        self.width = width
        self.height = height
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.selected_square = None
        self.create_board()
        self.root.title('Chess Board')

    def create_board(self):
        self.squares = {}
        colors = ['#ebecd0', '#739552']
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                square = tk.Canvas(self.board_frame, width=self.width, height=self.height, bg=color)
                square.grid(row=row, column=col)
                square.bind('<Button-1>', lambda event, row=row, col=col: self.select_square(row, col))
                self.squares[(row, col)] = square

    def select_square(self, row, col):
        if self.selected_square:
            self.deselect_square()

        self.selected_square = (row, col)
        square = self.squares[self.selected_square]
        original_color = square.cget('bg')
        darkened_color = darken_color(original_color)
        square.configure(bg=darkened_color)

    def deselect_square(self):
        square = self.squares[self.selected_square]
        original_color = ['#ebecd0', '#739552'][(self.selected_square[0] + self.selected_square[1]) % 2]
        square.configure(bg=original_color)
        self.selected_square = None


if __name__ == '__main__':
    root = tk.Tk()
    board = ChessBoard(root)
    root.mainloop()
