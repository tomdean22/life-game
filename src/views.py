from tkinter import Canvas
from tkinter import BOTH, TOP


DARK = "#111a1e"
LIGHT = "#142229"
GREEN = "#6cd777"
ORANGE = "#D66825"
DARKORANGE = "#723612"

CANVAS_SIZE = 403, 600
CELL_SIZE = 20
ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)

formatRC = lambda r,c: f"({r},{c})"
flr = lambda id: id // COLUMNS if id % COLUMNS != 0 or id == 0 else id // COLUMNS - 1
md = lambda id: id % COLUMNS - 1 if id % COLUMNS != 0 else COLUMNS - 1

class GameDisplay:

    def __init__(self, master):
        print(f"ROWS/COLUMNS: {formatRC(ROWS, COLUMNS)}")
        self.canv = Canvas(master, height=CANVAS_SIZE[0], width=CANVAS_SIZE[1], bg=DARK)
        self.recs = self.create_squares()

        self.canv.bind('<ButtonPress-1>', self.select_square)
        self.canv.pack(fill=BOTH)
    
    def select_square(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        id_ = canvas.find_closest(x, y)[0]

        row = event.y // CELL_SIZE
        column = event.x // CELL_SIZE
        key = formatRC(row, column)
        print(f"\n[select_square(0)]: {id_} at location: {key}")

        try:
            color = self.canv.itemcget(self.recs[key], option="fill")
        except KeyError:
            print(f"[select_square(1)]: {key} -outside grid")
        else:
            fill = ORANGE if color == LIGHT else LIGHT
            activefill = ORANGE if fill == ORANGE else DARKORANGE
            tag = "alive" if fill == ORANGE else "dead"
            self.canv.itemconfig(self.recs[key], fill=fill, activefill=activefill, tags=tag)

    def create_squares(self):
        recs = dict()
        y = 4
        for row in range(ROWS):
            x = 4
            for column in range(COLUMNS):
                recs[formatRC(row,column)] = self.canv\
                    .create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
                    fill=LIGHT, outline=ORANGE, activefill=DARKORANGE, tags="dead")
                x += CELL_SIZE
            y += CELL_SIZE
        return recs

    def collect_squares(self):
        alive_cells = self.canv.find_withtag("alive")
        return list((flr(i), md(i)) for i in alive_cells)

    def display_squares(self, live_cells):
        print(f"\n[display_squares(1)]: {live_cells} type: {type(live_cells[0])}")
        live_cells = [formatRC(*cell) for cell in live_cells]
        print(f"[display_squares(2)]:")
        opts = None
        for row in range(ROWS):
            for column in range(COLUMNS):
                key = formatRC(row,column)
                if key in live_cells:
                    print(f"  {key}")
                    opts = {k:v for k,v in zip(['fill', 'activefill','tags'],
                                                [ORANGE, ORANGE, 'alive']) }
                else:
                    opts = {k:v for k,v in zip(['fill', 'activefill','tags'],
                                                [LIGHT, DARKORANGE, 'dead']) }
                self.canv.itemconfig(self.recs[key], **opts)

