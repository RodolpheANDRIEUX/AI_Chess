import tkinter as tk


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 1
        self.y = -1

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= self.canvas.winfo_height():
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas.winfo_width():
            self.x = -self.x


class AnimationWindow:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title("Animation Example")
        self.canvas = tk.Canvas(self.tk, width=500, height=400, bd=0)
        self.canvas.pack()
        self.ball = Ball(self.canvas, 'red')

    def animate(self):
        while True:
            self.ball.draw()
            self.tk.update_idletasks()
            self.tk.update()
            self.tk.after(1)


if __name__ == "__main__":
    window = AnimationWindow()
    window.animate()
