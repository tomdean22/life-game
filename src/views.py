from tkinter import Canvas
from tkinter import BOTH, TOP
from .helpers import State, Colors, Configuration as config

class GameDisplay:

    def __init__(self, master: 'Tk()'):
        print(f"ROWS/COLUMNS: {config.formatRC(config.ROWS, config.COLUMNS)}")
        self.canv = Canvas(master, height=config.CANVAS_SIZE[0],
                                   width=config.CANVAS_SIZE[1],
                                   bg=Colors.DARK)
        self._all_cells = None
        self.create_cells()

        self.canv.bind('<ButtonPress-1>', self.select_cell)
        self.canv.pack(fill=BOTH)
    

    def create_cells(self):
        """ Draw, configure and store a grid of cells on the Tkinter Canvas """
        self._all_cells = dict()
        y = 4
        for row in range(config.ROWS):
            x = 4
            for column in range(config.COLUMNS):
                self._all_cells[config.formatRC(row,column)] = self.canv\
                    .create_rectangle(x, y, x+config.CELL_SIZE, y+config.CELL_SIZE,
                    config.set_opts(State.DEAD))
                x += config.CELL_SIZE
            y += config.CELL_SIZE

    def get_live_cells(self):
        """ Collect cells from gamedisplay to be used as the seed """
        alive_cells = self.canv.find_withtag(State.ALIVE)
        return list((config.flr(i), config.md(i)) for i in alive_cells)

    def reset_cells(self):
        """ Change the cell configurations from State.ALIVE to State.DEAD """
        for cell in self.canv.find_withtag(State.ALIVE):
            self.canv.itemconfig(cell, **config.set_opts(State.DEAD))

    def select_cell(self, event: '<Button-1> Clicked'):
        """
        Change the state of the cell from State.DEAD to State.ALIVE and vice versa 
        
        Parameters:
            event: automatically included argument, contains event and widget info
        """
        canvas = event.widget
        x = canvas.canvasx(event.x) 
        y = canvas.canvasy(event.y)
        id_ = canvas.find_closest(x, y)[0]

        row = event.y // config.CELL_SIZE
        column = event.x // config.CELL_SIZE
        key = config.formatRC(row, column)
        print(f"[views.GameDisplay.select_cell]: {id_} at location: {key}")

        try:
            color = self.canv.itemcget(self._all_cells[key], option="fill")
        except KeyError:
            print(f"[views.GameDisplay.select_cell]: {key} -- outside grid")
        else:
            if color == Colors.LIGHT:
                opts = config.set_opts(State.ALIVE)
            else:
                opts = config.set_opts(State.DEAD)

            self.canv.itemconfig(self._all_cells[key], **opts)

    def display_cells(self, live_cells: [(1,2), (3,4)]=None):
        """
        Update the game display
        
        Parameters:
            live_cells: list of live cells as (row, column) tuples            
        """
        if live_cells is None:
            live_cells = []
        else:
            live_cells = [config.formatRC(*cell) for cell in live_cells]
            print(f"[views.GameDisplay.display_cells]: {live_cells}")
        
        o = None
        for row in range(config.ROWS):
            for column in range(config.COLUMNS):
                key = config.formatRC(row,column)
                if key in live_cells:
                    o = config.set_opts(State.ALIVE)
                else:
                    o = config.set_opts(State.DEAD)
                self.canv.itemconfig(self._all_cells[key], **o)

