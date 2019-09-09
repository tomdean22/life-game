from functools import partial
from tkinter import Tk, LabelFrame, Button, BOTTOM, BOTH, Y
from src.views import GameDisplay, GREEN, DARK, CANVAS_SIZE
from src.game_of_life import Game

height = CANVAS_SIZE[0] + 60
width = CANVAS_SIZE[1] + 13

game = Game()

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

def updateGenLoop(game, display):
    pass

def main():
    master = Tk()
    baseFrame = LabelFrame(master, bg=DARK)
    gamedisplay = GameDisplay(baseFrame)
    
    Button(baseFrame, bg=DARK, text="Update Gen Once",
                      font="Silom 12 bold", bd=0, fg=GREEN,
                      highlightcolor=DARK, highlightbackground=DARK,
                      highlightthickness=0, command=lambda: updateGenCallback(game, gamedisplay)).pack(fill=Y)

    baseFrame.pack(fill=BOTH, side=BOTTOM)
    master.update()
    master.resizable(False, False)
    master.after(0, master.geometry(f"{width}x{height}"))
    master.mainloop()
