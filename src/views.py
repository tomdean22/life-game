from tkinter import Canvas
from tkinter import BOTH, TOP


DARK = "#111a1e"
LIGHT = "#142229"
GREEN = "#6cd777"
ORANGE = "#D66825"
DARKORANGE = "#723612"

CANVAS_SIZE = 600, 403
CELL_SIZE = 20
ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)
formatRC = lambda r,c: f"({r},{c})"

class GameDisplay:

    def __init__(self, master):
        print(f"ROWS/COLUMNS: {formatRC(ROWS, COLUMNS)}")
        self.canv = Canvas(master, width=CANVAS_SIZE[0], height=CANVAS_SIZE[1], bg=DARK)
        self.recs = self.create_squares()

        self.canv.bind('<ButtonPress-1>', self.check_squares)
        self.canv.pack(fill=BOTH)
    
    def check_squares(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        id_ = canvas.find_closest(x, y)[0]

        row = event.x // CELL_SIZE
        column = event.y // CELL_SIZE
        key = formatRC(row, column)
        print(f"checked square: {id_} at location: {key}")

        try:
            color = self.canv.itemcget(self.recs[key], option="fill")
        except KeyError:
            print(f"Click outside grid: {key}")
        else:
            fill = ORANGE if color == LIGHT else LIGHT
            activefill = ORANGE if fill == ORANGE else DARKORANGE
            tag = "alive" if fill == ORANGE else "dead"
            self.canv.itemconfig(self.recs[key], fill=fill, activefill=activefill, tags=tag)

    def create_squares(self):
        recs = dict()
        x = 4
        for row in range(ROWS):
            y = 4
            for column in range(COLUMNS):
                recs[formatRC(row,column)] = self.canv\
                    .create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
                    fill=LIGHT, outline=ORANGE, activefill=DARKORANGE, tags="dead")
                y += CELL_SIZE
            x += CELL_SIZE
        return recs

    def collect_squares(self):
        print(self.canv.find_withtag("alive"))
