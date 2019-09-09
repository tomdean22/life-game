from functools import partial
from tkinter import Tk, LabelFrame, Button, BOTTOM, BOTH, Y
from src.views import GameDisplay, GREEN, DARK, CANVAS_SIZE
from src.game_of_life import Game

width = CANVAS_SIZE[0] + 13
height = CANVAS_SIZE[1] + 60

game = Game()

def updateGenCallback():
    # collect live cells from board

    # initialize game with cells

    # update generation
    game.update_board()

    # collect live cells
    live_cells = game.get_live_cells()

    # change cell color

def main():
    master = Tk()
    baseFrame = LabelFrame(master, bg=DARK)
    gamedisplay = GameDisplay(baseFrame)
    
    Button(baseFrame, bg=DARK, text="Update Gen Once",
                      font="Silom 12 bold", bd=0, fg=GREEN,
                      highlightcolor=DARK, highlightbackground=DARK,
                      highlightthickness=0, command=lambda: gamedisplay.collect_squares()).pack(fill=Y)

    baseFrame.pack(fill=BOTH, side=BOTTOM)
    master.update()
    master.resizable(False, False)
    master.after(0, master.geometry(f"{width}x{height}"))
    master.mainloop()
