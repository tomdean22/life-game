from time import sleep
from functools import partial
from tkinter import Tk, LabelFrame, Button, Checkbutton
from tkinter import LEFT, RIGHT, BOTTOM, BOTH, Y
from src.views import GameDisplay
from src.helpers import Const
from src.game_of_life import Game

height = Const.CANVAS_SIZE[0] + 60
width = Const.CANVAS_SIZE[1] + 13

game = Game()

master = Tk()
baseFrame = LabelFrame(master, bg=Const.DARK)
display = GameDisplay(baseFrame)

loop = False

def updateGenCallback():
    # collect live cells from GUI
    live_cells = display.get_live_squares()
    print(f"\n[updateGenCallback(1)]: {live_cells}")

    # initialize game with cells
    game.initialize_board_from_seed(live_cells)
    del(live_cells)
    # update generation
    game.update_board()
    # collect live cells
    live_cells = game.get_live_cells()
    print(f"[updateGenCallback(2)]: {live_cells}")

    # change cell color
    display.display_squares(live_cells)

    if loop:
        master.after(500, updateGenCallback)

def loop_switch(thisBtn, thatBtn):
    global loop
    loop = False if loop else True
    if loop:
        thatBtn.invoke()
        thatBtn.config(state="disabled")
        thisBtn.config(bg=Const.GREEN)
    else:
        thatBtn.config(state="active")

def reset():
    game.initialize_board_from_seed(seed=None)
    display.reset_squares()

def main():
    btn_opts = {k:v for k,v in zip(['bg', 'font','bd','fg','highlightcolor',
                                   'highlightbackground', 'highlightthickness'],
                                  [Const.DARK, 'Silom 12 bold', 0, Const.GREEN, Const.DARK, Const.DARK, 0])}
    
    b1 = Button(baseFrame, **btn_opts,
                           text="Update",
                           command=updateGenCallback)
    
    b2 = Button(baseFrame, **btn_opts,
                           text="Update Loop",
                           command=lambda: loop_switch(b2, b1))
                           
    b3 = Button(baseFrame, **btn_opts,
                           text="Quit",
                           command=master.quit)

    b4 = Button(baseFrame, **btn_opts,
                           text="Clear",
                           command=reset)

    b1.pack(fill=Y, side=LEFT)
    b2.pack(fill=Y, side=LEFT)
    b3.pack(fill=Y, side=RIGHT)
    b4.pack(fill=Y, side=RIGHT)

    baseFrame.pack(fill=BOTH, side=BOTTOM)
    master.update()
    master.resizable(False, False)
    master.after(0, master.geometry(f"{width}x{height}"))
    master.mainloop()
