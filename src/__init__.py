from time import sleep
from functools import partial
from tkinter import Tk, LabelFrame, Button, Checkbutton
from tkinter import LEFT, RIGHT, BOTTOM, BOTH, Y
from src.views import GameDisplay, GREEN, DARK, CANVAS_SIZE
from src.game_of_life import Game

height = CANVAS_SIZE[0] + 60
width = CANVAS_SIZE[1] + 13

game = Game()

master = Tk()
baseFrame = LabelFrame(master, bg=DARK)
display = GameDisplay(baseFrame)

loop = False

def updateGenCallback():
    # collect live cells from GUI
    live_cells = display.get_live_squares()
    print(f"\n[updateGenCallback(1)]: {live_cells} type: {type(live_cells[0])}")

    # initialize game with cells
    game.initialize_board_from_seed(live_cells)
    del(live_cells)
    # update generation
    game.update_board()
    # collect live cells
    live_cells = game.get_live_cells()
    print(f"\n[updateGenCallback(2)]: {live_cells}, type: {type(live_cells[0])}")

    # change cell color
    display.display_squares(live_cells)

    if loop:
        master.after(500, updateGenCallback)

def loop_switch(btn):
    global loop
    loop = False if loop else True
    if loop:
        btn.invoke()
        btn.config(state="disabled")
    else:
        btn.config(state="active")

def reset():
    game.initialize_board_from_seed()
    display.create_squares()

def main():
    btn_opts = {k:v for k,v in zip(['bg', 'font','bd','fg','highlightcolor',
                                   'highlightbackground', 'highlightthickness'],
                                  [DARK, 'Silom 12 bold', 0, GREEN, DARK, DARK, 0])}
    
    b1 = Button(baseFrame, **btn_opts,
                           text="Update",
                           command=updateGenCallback)
    
    b2 = Checkbutton(baseFrame, bg=DARK,
                           font='Silom 12 bold',
                           text="Loop",
                           command=lambda: loop_switch(b1))
                           
    b3 = Button(baseFrame, **btn_opts,
                           text="Quit",
                           command=master.quit)

    b4 = Button(baseFrame, **btn_opts,
                           text="Clear",
                           command=lambda: game.initialize_board_from_seed())

    b1.pack(fill=Y, side=LEFT)
    b2.pack(fill=Y, side=LEFT)
    b3.pack(fill=Y, side=RIGHT)

    baseFrame.pack(fill=BOTH, side=BOTTOM)
    master.update()
    master.resizable(False, False)
    master.after(0, master.geometry(f"{width}x{height}"))
    master.mainloop()
