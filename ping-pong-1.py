from tkinter import *
from random import randint
from time import sleep


class Ball:
    def __init__(self, canvas, color, platform):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = randint(-3, 3)
        self.y = randint(-3, 3)
        self.platform = platform
        self.touch_bottom = False

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        coords = self.canvas.coords(self.oval)
        if coords[0] <= 0: self.x *= -1
        if coords[1] <= 0: self.y *= -1
        if coords[2] >= 500: self.x *= -1
        if coords[3] >= 400: self.touch_bottom = True
        if self.touch_platform(coords):
            self.y *= -1

    def touch_platform(self, ball_coords):
        platform_coords = self.canvas.coords(self.platform.rect)
        if ball_coords[0] >= platform_coords[0] and ball_coords[2] <= platform_coords[2] and platform_coords[1] <= ball_coords[3] <= platform_coords[3]:
            return True
        return False


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(200, 300, 300, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.__left)
        self.canvas.bind_all('<KeyPress-Right>', self.__right)

    def __left(self, event):
        self.x = -2

    def __right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        coords = self.canvas.coords(self.rect)
        if coords[0] <= 0: self.x = 0
        if coords[2] >= 500: self.x = 0


window = Tk()
window.title('Mini ping-pong')
window.resizable(0, 0)
window.wm_attributes('-topmost', 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'green')
ball = Ball(canvas, 'red', platform)
while True:
    if not ball.touch_bottom:
        ball.draw()
        platform.draw()
        window.update()
        sleep(0.01)
    else:
        break
