from enum import Enum, auto

class State(Enum):
    DEAD = auto()
    ALIVE = auto()


class Trigger(Enum):
    JUSTRIGHT     = lambda i,j,g: g.count_neighbors(i,j) == 3
    BADPOPULATION = lambda i,j,g: g.count_neighbors(i,j) < 2 or g.count_neighbors(i,j) > 3


class Colors:
    DARK = "#111a1e"
    LIGHT = "#142229"
    WHITE = "#ffffff"
    GREEN = "#6cd777"
    ORANGE = "#D66825"
    DARKORANGE = "#723612"


class Configuration:

    """ GameDisplay settings for Conway's Game of Life """

    # GameDisplay dimensions
    CANVAS_SIZE = 393, 600
    CELL_SIZE = 15
    ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)

    # Format the row, column to use as a key
    # Use each cell's id to compute (row, column) key
    formatRC = lambda r,c: f"({r},{c})"
    flr = lambda id: id // Configuration.COLUMNS if id % Configuration.COLUMNS != 0 \
        or id == 0 else id // Configuration.COLUMNS - 1
    md = lambda id: id % Configuration.COLUMNS - 1 if id % Configuration.COLUMNS != 0 else Configuration.COLUMNS - 1

    # presets for State.DEAD and State.ALIVE
    options = ['fill', 'activefill', 'outline','tags']
    vals_alive = [Colors.ORANGE, Colors.ORANGE, Colors.WHITE, State.ALIVE]
    vals_dead = [Colors.LIGHT, Colors.DARKORANGE, Colors.ORANGE, State.DEAD]
    set_opts = lambda s: {k:v for k,v in zip(Configuration.options, Configuration.vals_dead)} if s == State.DEAD \
        else {k:v for k,v in zip(Configuration.options, Configuration.vals_alive)}
