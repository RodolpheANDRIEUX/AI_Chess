import tkinter as tk

from chess.game import Game
from gui.board_view import BoardView


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.game = Game()
        self.board_view = BoardView(self, self.game)


class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.menu = MyFrame(self)
        self.configure(bg='#ebecd0')
        self.menu.grid(row=1, column=0, padx=200, pady=20)


class MyButton(tk.Button):

    def __init__(self, master, id):
        self.id = id
        tk.Button.__init__(self, master, text=self.id)
        self.configure(width=20, height=2)
        self.configure(bg='#739552', fg='#ebecd0')
        self.configure(font=('Times New Roman', 20, 'italic'))
        self.configure(command=self.fonction)
        self.configure(activebackground='#b9ca43', activeforeground='#ebecd0')
        self.configure(relief=tk.RIDGE, bd=3)
        self.configure(cursor='hand2')

    def fonction(self):
        if self.id == '2 joueurs':
            for widget in self.master.master.winfo_children():
                widget.destroy()
            app = MainWindow(self.master.master)
            app.grid()


class MyFrame(tk.Frame):

    def __init__(self, master, ):
        tk.Frame.__init__(self, master)
        self.button_list = [MyButton(self, id) for id in ('1 joueur', '2 joueurs', 'Settings')]
        self.configure(bg='#ebecd0')
        for k, button in enumerate(self.button_list):
            button.grid(row=k, column=0, padx=20, pady=20)
