from tkinter import Tk, Label, LabelFrame, Button
from tkinter import LEFT, RIGHT, BOTTOM, TOP, BOTH, Y, X
from src.helpers import Colors, Configuration as config
from src.views import GameDisplay
from src.gameoflife import Game


class Controller:
    """
    This class is the interface between gameoflife.Game and views.GameDisplay

    Attributes:
        height, width: dimensions of the master Tk() frame
        master: root Tk() window
        baseframe: holds title, gamedisplay and buttons
        loop: Boolean for looping through generations or advancing one by one
        btn_opts: Dictionary for default button configurations
        game: Conway's Game of Life -> instance of Game class
        updateBtn: update current board to the next generation according to Conway's rules
        updateLoopBtn: trigger loop_switch callback
        quitBtn: close application
        clearBtn: reset display and game board
    """
    height = config.CANVAS_SIZE[0] + 66
    width = config.CANVAS_SIZE[1] + 13

    master = Tk()
    master.title("Conway's Game of Life")
    baseFrame = LabelFrame(master, bg=Colors.DARK)
    titleLbl = Label(baseFrame, text="The Game of Life", fg=Colors.GREEN,
                                bg=Colors.DARK, font="Silom 18 bold").pack(fill=X, side=TOP)
    gamedisplay = GameDisplay(baseFrame)
    loop = False

    btn_opts = {
        'bg': Colors.DARK,
        'font': 'Silom 12 bold',
        'bd': 0,
        'fg': Colors.GREEN,
        'highlightcolor': Colors.DARK,
        'highlightbackground': Colors.DARK,
        'highlightthickness': 0
    }

    def __init__(self):
        """ Create user interface for Conway's Game of Life """
        self.game = Game()
        
        self.updateBtn = Button(Controller.baseFrame, **Controller.btn_opts,
                            text="Update",
                            command=self.update_callback)
        
        self.updateLoopBtn = Button(Controller.baseFrame, **Controller.btn_opts,
                            text="Update Loop",
                            command=self.loop_switch)
                            
        self.quitBtn = Button(Controller.baseFrame, **Controller.btn_opts,
                            text="Quit",
                            command=Controller.master.quit)

        self.clearBtn = Button(Controller.baseFrame, **Controller.btn_opts,
                            text="Clear",
                            command=self.reset)

        self.updateBtn.pack(fill=Y, side=LEFT)
        self.updateLoopBtn.pack(fill=Y, side=LEFT)
        self.quitBtn.pack(fill=Y, side=RIGHT)
        self.clearBtn.pack(fill=Y, side=RIGHT)
        Controller.baseFrame.pack(fill=BOTH, side=BOTTOM)

        Controller.master.update()
        Controller.master.resizable(False, False)
        Controller.master.after(0, Controller.master.geometry(f"{Controller.width}x{Controller.height}"))
        Controller.master.mainloop()


    def update_callback(self):
        """ Get the seed from gamedisplay, initialize and update the board, then update the display """
        live_cells = Controller.gamedisplay.get_live_cells()
        print(f"[__init__.Controller.update_callback<GameDisplay>]: {live_cells}")

        self.game.initialize_board_from_seed(live_cells)
        del(live_cells)
        self.game.update_board()
        live_cells = self.game.get_live_cells()
        print(f"[__init__.Controller.update_callback<Game>]: {live_cells}")

        Controller.gamedisplay.display_cells(live_cells)

        if Controller.loop:
            Controller.master.after(500, self.update_callback)

    def loop_switch(self):
        """ Switch to control looping through generations instead of one at a time. """
        Controller.loop = False if Controller.loop else True
        if Controller.loop:
            self.updateBtn.invoke()
            self.updateBtn.config(state="disabled")
            self.clearBtn.config(state="disabled")

            self.updateLoopBtn.config(bg=Colors.GREEN)
        else:
            self.updateBtn.config(state="active")
            self.clearBtn.config(state="active")

    def reset(self):
        """ reset all cells in game.board and gamedisplay._all_cells to State.DEAD """
        self.game.initialize_board_from_seed(seed=None)
        Controller.gamedisplay.reset_cells()
