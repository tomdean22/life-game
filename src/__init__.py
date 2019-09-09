from time import sleep
from functools import partial
from tkinter import Tk, LabelFrame, Button, LEFT, RIGHT, BOTTOM, BOTH, Y
from src.views import GameDisplay, GREEN, DARK, CANVAS_SIZE
from src.game_of_life import Game

height = CANVAS_SIZE[0] + 60
width = CANVAS_SIZE[1] + 13

game = Game()
master = Tk()

loop = False

def updateGenCallback(game, display):
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
        master.after(500, lambda: updateGenCallback(game, display))

def start_loop(game, display):
    global loop
    loop = True
    updateGenCallback(game, display)

def stop_loop(game, display):
    global loop
    loop = False

def main():
    baseFrame = LabelFrame(master, bg=DARK)
    gamedisplay = GameDisplay(baseFrame)
    btn_opts = {k:v for k,v in zip(['bg', 'font','bd','fg','highlightcolor',
                                   'highlightbackground', 'highlightthickness'],
                                  [DARK, 'Silom 12 bold', 0, GREEN, DARK, DARK, 0])}
    
    b1 = Button(baseFrame, **btn_opts,
                           text="Update Gen Once",
                           command=lambda: updateGenCallback(game, gamedisplay))
    
    b2 = Button(baseFrame, **btn_opts,
                           text="Stop Loop",
                           command=lambda: stop_loop(game, gamedisplay))
                           
    b3 = Button(baseFrame, **btn_opts,
                           text="Start Loop",
                           command=lambda: start_loop(game, gamedisplay))

    b1.pack(fill=Y, side=LEFT)
    b2.pack(fill=Y, side=RIGHT)
    b3.pack(fill=Y, side=RIGHT)

    baseFrame.pack(fill=BOTH, side=BOTTOM)
    master.update()
    master.resizable(False, False)
    master.after(0, master.geometry(f"{width}x{height}"))
    master.mainloop()
