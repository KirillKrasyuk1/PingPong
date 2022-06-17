from tkinter import *
import time
import random


class Platform(object):
    def __init__(self, canvas, platform_color, width, height):
        self.canvas = canvas
        self.x = 0
        self.platform = canvas.create_rectangle(width / 2 - 45, height - 55, width / 2 + 45, height - 75, fill = platform_color)
        self.canvas_width = width
        #ToDo почему то не работает.
        self.canvas.bind_all('<KeyPress-Left>', self.left_movement)
        self.canvas.bind_all('<KeyPress-Right>', self.right_movement)

    def left_movement(self, evt):
        self.x = -2

    def right_movement(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.platform, self.x, 0)
        pos = self.canvas.coords(self.platform) # returns(x1, y1, x2, y2 - left corner, right corner)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


    # def left_movement(self, evt):
    #    if event.keysim == 'Left':
    #        event.move(platform, 0, -5)
class Ball(object):
    def __init__(self, canvas, ball_color, width, height):
        self.canvas = canvas
        direct = [-3, -2, -1, 1, 2, 3]
        self.x = RndDirection(direct)
        self.y = RndDirection(direct)
        self.canvas_height = height
        self.canvas_width = width
        self.ball = canvas.create_oval(width / 2 - 15, height / 2 - 15, width / 2 + 15,height / 2 + 15 , fill = ball_color)


    def draw(self):
        self.canvas.move(self.ball, self.x, self.y)
        pos = self.canvas.coords(self.ball)
        print(pos, self.canvas_height)
        if pos[1] <= 0:
            self.y = RndDirection([3, 2, 1])
        if pos[3] >= self.canvas_height:
            self.y = RndDirection([-3, -2, -1])
        if pos[0] <= 0:
            self.x = RndDirection([3, 2, 1])
        if pos[2] >= self.canvas_width:
            self.x = RndDirection([-3, -2, -1])
def RndDirection(ListOfDirections):
    return random.choice(ListOfDirections)
wh, ht = 800, 800
tk = Tk()
tk.title('Пинг понг')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = wh, height = ht)
canvas.pack()
ball = Ball(canvas, 'red', wh, ht)
platform = Platform(canvas, 'blue', wh, ht)
while 1:
    ball.draw()
    tk.update()
    tk.update_idletasks()
    time.sleep(0.01)
    #tk.mainloop()