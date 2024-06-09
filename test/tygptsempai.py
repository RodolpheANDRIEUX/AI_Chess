import tkinter as tk
from PIL import Image, ImageTk


class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")

        self.square_size = 75
        self.canvas = tk.Canvas(self.root, width=self.square_size * 8, height=self.square_size * 8)
        self.canvas.pack()

        self.board_images = {}
        self.load_images()

        self.draw_board()
        self.place_pieces()

    def load_images(self):
        pieces = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
        for piece in pieces:
            image = Image.open(f"../pieces/{piece}.png")
            image = image.resize((self.square_size, self.square_size))
            self.board_images[piece] = ImageTk.PhotoImage(image)

    def draw_board(self):
        colors = ['white', 'gray']
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x0 = col * self.square_size
                y0 = row * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def place_pieces(self):
        initial_positions = {
            'bp': [(1, i) for i in range(8)],
            'wp': [(6, i) for i in range(8)],
            'br': [(0, 0), (0, 7)],
            'wr': [(7, 0), (7, 7)],
            'bn': [(0, 1), (0, 6)],
            'wn': [(7, 1), (7, 6)],
            'bb': [(0, 2), (0, 5)],
            'wb': [(7, 2), (7, 5)],
            'bq': [(0, 3)],
            'wq': [(7, 3)],
            'bk': [(0, 4)],
            'wk': [(7, 4)]
        }

        for piece, positions in initial_positions.items():
            for position in positions:
                x = position[1] * self.square_size + self.square_size // 2
                y = position[0] * self.square_size + self.square_size // 2
                self.canvas.create_image(x, y, image=self.board_images[piece], anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
