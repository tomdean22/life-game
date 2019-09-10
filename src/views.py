from tkinter import Canvas
from tkinter import BOTH, TOP
from .helpers import State, Const

class GameDisplay:

    def __init__(self, master: 'Tk()'):
        print(f"ROWS/COLUMNS: {Const.formatRC(Const.ROWS, Const.COLUMNS)}")
        self.canv = Canvas(master, height=Const.CANVAS_SIZE[0],
                                   width=Const.CANVAS_SIZE[1],
                                   bg=Const.DARK)
        self.create_cells()

        self.canv.bind('<ButtonPress-1>', self.select_cell)
        self.canv.pack(fill=BOTH)
    
    def select_cell(self, event: '<Button-1> Clicked'):
        canvas = event.widget
        x = canvas.canvasx(event.x) 
        y = canvas.canvasy(event.y)
        id_ = canvas.find_closest(x, y)[0]

        row = event.y // Const.CELL_SIZE
        column = event.x // Const.CELL_SIZE
        key = Const.formatRC(row, column)
        print(f"[views.GameDisplay.select_cell]: {id_} at location: {key}")

        try:
            color = self.canv.itemcget(self._all_cells[key], option="fill")
        except KeyError:
            print(f"[views.GameDisplay.select_cell]: {key} -- outside grid")
        else:
            if color == Const.LIGHT:
                opts = Const.set_opts(State.ALIVE)
            else:
                opts = Const.set_opts(State.DEAD)

            self.canv.itemconfig(self._all_cells[key], **opts)

    def create_cells(self):
        """ Draw, configure and store a grid of cells on the Tkinter Canvas """
        self._all_cells = dict()
        y = 4
        for row in range(Const.ROWS):
            x = 4
            for column in range(Const.COLUMNS):
                self._all_cells[Const.formatRC(row,column)] = self.canv\
                    .create_rectangle(x, y, x+Const.CELL_SIZE, y+Const.CELL_SIZE,
                    Const.set_opts(State.DEAD))
                x += Const.CELL_SIZE
            y += Const.CELL_SIZE

    def reset_cells(self):
        """ Change the cell configurations from State.ALIVE to State.DEAD """
        for cell in self.canv.find_withtag(State.ALIVE):
            self.canv.itemconfig(cell, **Const.set_opts(State.DEAD))

    def get_live_cells(self):
        """ Collect cells from the display to be used as the seed """
        alive_cells = self.canv.find_withtag(State.ALIVE)
        return list((Const.flr(i), Const.md(i)) for i in alive_cells)

    def display_cells(self, live_cells: [(1,2), (3,4)]=None):
        """ Receive updated list of live cells to display in GameDisplay """
        if live_cells is None:
            live_cells = []
        else:
            live_cells = [Const.formatRC(*cell) for cell in live_cells]
            print(f"[views.GameDisplay.display_cells]: {live_cells}")
        
        o = None
        for row in range(Const.ROWS):
            for column in range(Const.COLUMNS):
                key = Const.formatRC(row,column)
                if key in live_cells:
                    o = Const.set_opts(State.ALIVE)
                else:
                    o = Const.set_opts(State.DEAD)
                self.canv.itemconfig(self._all_cells[key], **o)

