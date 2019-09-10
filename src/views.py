from tkinter import Canvas
from tkinter import BOTH, TOP
from .helpers import State, Colors, Config as cnf

class GameDisplay:

    def __init__(self, master: 'Tk()'):
        print(f"ROWS/COLUMNS: {cnf.formatRC(cnf.ROWS, cnf.COLUMNS)}")
        self._canv = Canvas(master, height=cnf.CANVAS_SIZE[0],
                                   width=cnf.CANVAS_SIZE[1],
                                   bg=Colors.DARK)
        self._all_cells = dict()
        self._create_cells()

        self._canv.bind('<ButtonPress-1>', self.select_cell)
        self._canv.pack(fill=BOTH)
    

    def _create_cells(self):
        """ Draw, configure and store a grid of cells on the Tkinter Canvas """
        linear_pos = 1
        y = cnf.STARTPOS
        for row in range(cnf.ROWS):
            x = cnf.STARTPOS
            for column in range(cnf.COLUMNS):
                self._all_cells[linear_pos] = self._canv.create_rectangle(
                    x, y, x+cnf.CELL_SIZE, y+cnf.CELL_SIZE,
                    cnf.set_opts(State.DEAD))
                linear_pos += 1
                x += cnf.CELL_SIZE
            y += cnf.CELL_SIZE

    def get_live_cells(self):
        """ Collect cells from gamedisplay to be used as the seed """
        return self._canv.find_withtag(State.ALIVE)

    def reset_cells(self):
        """ Change all cells to State.DEAD """
        for cell in self._canv.find_withtag(State.ALIVE):
            self._canv.itemconfig(cell, **cnf.set_opts(State.DEAD))

    def select_cell(self, event: '<Button-1> Clicked'):
        """
        Switch the state of the cell between State.DEAD to State.ALIVE 
        
        Parameters:
            event: automatically included argument, contains event and widget info
        """
        id_ = cnf.getID(event)
        rc  = cnf.getRC(event)

        print(f"[views.GameDisplay.select_cell]: {id_} at location: {rc}")

        try:
            color = self._canv.itemcget(self._all_cells[id_], option="fill")
        except KeyError:
            print(f"[views.GameDisplay.select_cell]: {rc} -- outside grid")
        else:
            if color == Colors.LIGHT:
                opts = cnf.set_opts(State.ALIVE)
            else:
                opts = cnf.set_opts(State.DEAD)

            self._canv.itemconfig(self._all_cells[id_], **opts)

    def display_cells(self, live_cells: [1,223,405]=None, opts=None):
        """
        Update the game display
        
        Parameters:
            live_cells: list of live cell ids            
        """
        if live_cells is None:
            live_cells = []
        else:
            print(f"[views.GameDisplay.display_cells]: {live_cells}")

        linear_pos = 1
        for row in range(cnf.ROWS):
            for column in range(cnf.COLUMNS):
                if linear_pos in live_cells:
                    opts = cnf.set_opts(State.ALIVE)
                else:
                    opts = cnf.set_opts(State.DEAD)
                self._canv.itemconfig(self._all_cells[linear_pos], **opts)
                linear_pos += 1

