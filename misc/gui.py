from tkinter import Tk
from tkinter import Canvas, LabelFrame, Frame
from tkinter import Label, Button
from tkinter import X, CENTER, LEFT, RIGHT, BOTH, BOTTOM, TOP
from tkinter import RAISED, GROOVE, SUNKEN, FLAT

from functools import partial

from src.game_of_life import ROWS, COLUMNS
from src.game_of_life import Game


# THEME
DARK = "#111a1e"
GREEN = "#6cd777"
LIGHT = "#142229"
ORANGE = "#D66825"
DARKORANGE = "#723612"

# APP DISPLAY
MASTER_SZ = M_WIDTH, M_HEIGHT = 620, 600

# GAME DISPLAY
CANVAS_SIZE = 280, 380
CELL_SIZE = 20

# PARTIALS (functions with some preset parameters)
LF_dark = partial(LabelFrame, bd=3, relief=GROOVE, bg=DARK, fg=GREEN)
L_dark = partial(Label, bd=3, relief=GROOVE, bg=DARK, fg=GREEN)

master = Tk()

class GameDisplay:
    ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)
    formatRC = lambda s,r,c: f"({r},{c})"

    def __init__(self, master):
        print(self.formatRC(ROWS, COLUMNS))
        self.canv = Canvas(master, width=CANVAS_SIZE[0], height=CANVAS_SIZE[1], bg=DARK)
        self.recs = self.create_squares()

        self.canv.bind('<ButtonPress-1>', self.check_squares)
        self.canv.pack(fill=BOTH, side=TOP, padx=3, pady=3)
    
    def check_squares(self, event):
        row = event.y // CELL_SIZE
        column = event.x // CELL_SIZE
        print(f"check squares: {self.formatRC(row,column)}")
        self.canv.itemconfig(self.recs[self.formatRC(row,column)], fill=ORANGE)

    def create_squares(self):
        recs = dict()
        y = 0
        # print("====== CREATE SQUARES ======")
        for row in range(self.ROWS):
            x = 0
            for column in range(self.COLUMNS):
                # print(self.formatRC(row,column))
                recs[self.formatRC(row,column)] = self.canv\
                    .create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
                    fill=LIGHT, outline=ORANGE, activefill=DARKORANGE)
                x += CELL_SIZE
            y += CELL_SIZE
        return recs


def main():
    baseFrame = LF_dark(master, padx=3, pady=3)

    titleFrame = LF_dark(baseFrame)
    title = L_dark(titleFrame, bd=0, text="The Game of Life", font="Silom 36 bold").pack()
    titleFrame.pack(fill=X, pady=(0,3), side=TOP)
    
    GameDisplay(baseFrame)

    seedBtnFrame = LF_dark(baseFrame)
    seedBtn = Button(seedBtnFrame, text="FEED ME", font="Silom 12 bold", bd=0, bg=DARK, fg=GREEN, command=master.quit,
                     highlightcolor=DARK, highlightbackground=DARK, highlightthickness=0)
    seedBtn.pack(side=BOTTOM, pady=3)
    seedBtnFrame.pack(fill=BOTH, side=BOTTOM, pady=(3,0))


    baseFrame.pack(fill=BOTH, expand=1)

    master.update()
    master.resizable(False, False)
    master.geometry(f"{MASTER_SZ[[0]]}x{MASTER_SZ[1]}+50+250")
    # master.after(4000, lambda: master.quit())
    master.mainloop()
