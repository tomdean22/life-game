from tkinter import Tk, LabelFrame, Button
from tkinter import LEFT, RIGHT, BOTTOM, BOTH, Y
from src.views import GameDisplay
from src.helpers import Const
from src.game_of_life import Game


class Controller:
    height = Const.CANVAS_SIZE[0] + 60
    width = Const.CANVAS_SIZE[1] + 13

    master = Tk()
    baseFrame = LabelFrame(master, bg=Const.DARK)
    gamedisplay = GameDisplay(baseFrame)
    loop = False

    btn_opts = {k:v for k,v in zip(['bg', 'font','bd','fg','highlightcolor',
                                    'highlightbackground', 'highlightthickness'],
                                    [Const.DARK, 'Silom 12 bold', 0,
                                    Const.GREEN, Const.DARK, Const.DARK, 0])}

    def __init__(self):
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
        self.baseFrame.pack(fill=BOTH, side=BOTTOM)

        self.master.update()
        self.master.resizable(False, False)
        self.master.after(0, self.master.geometry(f"{Controller.width}x{Controller.height}"))
        self.master.mainloop()


    def update_callback(self):
        live_cells = Controller.gamedisplay.get_live_cells()
        print(f"\n[update_callback<GameDisplay>]: {live_cells}")

        self.game.initialize_board_from_seed(live_cells)
        del(live_cells)
        self.game.update_board()
        live_cells = self.game.get_live_cells()
        print(f"[update_callback<Game>]: {live_cells}")

        Controller.gamedisplay.display_cells(live_cells)

        if Controller.loop:
            Controller.master.after(500, self.update_callback)

    def loop_switch(self):
        Controller.loop = False if Controller.loop else True
        if Controller.loop:
            self.updateBtn.invoke()
            self.updateBtn.config(state="disabled")
            self.clearBtn.config(state="disabled")

            self.updateLoopBtn.config(bg=Const.GREEN)
        else:
            self.updateBtn.config(state="active")
            self.clearBtn.config(state="active")

    def reset(self):
        self.game.initialize_board_from_seed(seed=None)
        Controller.gamedisplay.reset_cells()
