import tkinter as tk
from PIL import Image, ImageTk

from chess.game import Game
from gui.board_view import BoardView


class MainWindow(tk.Frame):
    def __init__(self, player, master=None):
        super().__init__(master)
        self.game = Game(player)
        self.board_view = BoardView(self, self.game)


class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.background_color = '#312e2b'
        self.title_image = Image.open('gui/Title.png')
        self.title_image = ImageTk.PhotoImage(self.title_image)
        self.canvas = tk.Canvas(self, width=self.title_image.width(), height=self.title_image.height())
        self.canvas.create_image(0, 0, anchor='nw', image=self.title_image)
        self.canvas.config(bg=self.background_color, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.menu = MyFrame(self)
        self.configure(bg=self.background_color)
        self.menu.grid(row=1, column=0, padx=200, pady=20)


class MyButton(tk.Button):

    def __init__(self, master, id):
        self.id = id
        tk.Button.__init__(self, master, text=self.id)
        self.configure(width=15, height=1)
        self.configure(bg='#81b64c', fg='#ffffff')
        self.configure(font=('Arial', 25, 'bold'))
        self.configure(command=self.fonction)
        self.configure(activebackground='#b9ca43', activeforeground='#ffffff')
        self.configure(relief=tk.FLAT, bd=5)
        self.configure(cursor='hand2')

    def fonction(self):
        if self.id == '2 joueurs':
            for widget in self.master.master.winfo_children():
                widget.destroy()
            app = MainWindow(2, self.master.master)
            app.grid()
        elif self.id == '1 joueur':
            for widget in self.master.master.winfo_children():
                widget.destroy()
            app = MainWindow(1, self.master.master)
            app.grid()


class MyFrame(tk.Frame):

    def __init__(self, master, ):
        tk.Frame.__init__(self, master)
        self.button_list = [MyButton(self, id) for id in ('0 joueur', '1 joueur', '2 joueurs', 'Settings')]
        self.configure(bg='#eeeeee')
        for k, button in enumerate(self.button_list):
            button.grid(row=k, column=0, padx=20, pady=20)
