from enum import Enum, auto

class State(Enum):
    DEAD = auto()
    ALIVE = auto()


class Trigger(Enum):
    JUSTRIGHT     = lambda i,j,g: g.count_neighbors(i,j) == 3
    BADPOPULATION = lambda i,j,g: g.count_neighbors(i,j) < 2 or g.count_neighbors(i,j) > 3


class Colors:
    DARK       = "#111a1e"
    LIGHT      = "#142229"
    WHITE      = "#ffffff"
    GREEN      = "#6cd777"
    ORANGE     = "#D66825"
    DARKORANGE = "#723612"


class Config:

    """ GameDisplay settings for Conway's Game of Life """

    # GameDisplay dimensions
    CANVAS_SIZE   = 393, 600
    CELL_SIZE     = 15
    ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)
    STARTPOS = 4

    # Format the row, column to use as a key
    # Use each cell's id to compute (row, column) key
    formatRC      = lambda r,c: f"({r},{c})"
    flr           = lambda id: id // Config.COLUMNS if id % Config.COLUMNS != 0 \
                      else id // Config.COLUMNS - 1
    md            = lambda id: id % Config.COLUMNS - 1 if id % Config.COLUMNS != 0 \
                      else Config.COLUMNS - 1
    convertIDtoRC = lambda id: (Config.flr(id), Config.md(id))

    # views.GameDisplay.select_cell
    _getX = lambda e: e.widget.canvasx(e.x)
    _getY = lambda e: e.widget.canvasx(e.y)
    getID = lambda e: e.widget.find_closest(Config._getX(e),
                                            Config._getY(e))[0]

    _getRow    = lambda e: e.y // Config.CELL_SIZE
    _getColumn = lambda e: e.x // Config.CELL_SIZE
    getRC      = lambda e: Config.formatRC(Config._getRow(e),
                                           Config._getColumn(e))

    # __init__.Controller.update_callback
    no_change = lambda old, new: len(old) == len(new) and all([cell in old for cell in new])

    # presets for State.DEAD and State.ALIVE
    options    = ['fill', 'activefill', 'outline','tags']
    vals_alive = [Colors.ORANGE, Colors.ORANGE, Colors.WHITE, State.ALIVE]
    vals_dead  = [Colors.LIGHT, Colors.DARKORANGE, Colors.ORANGE, State.DEAD]
    set_opts   = lambda s: {k:v for k,v in zip(Config.options, Config.vals_dead)} if s == State.DEAD \
                   else {k:v for k,v in zip(Config.options, Config.vals_alive)}
