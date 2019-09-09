from enum import Enum, auto

class State(Enum):
    DEAD = auto()
    ALIVE = auto()


class Trigger(Enum):
    JUSTRIGHT     = lambda i,j,g: g.count_neighbors(i,j) == 3
    BADPOPULATION = lambda i,j,g: g.count_neighbors(i,j) < 2 or g.count_neighbors(i,j) > 3


class Const:
    DARK = "#111a1e"
    LIGHT = "#142229"
    WHITE = "#ffffff"
    GREEN = "#6cd777"
    ORANGE = "#D66825"
    DARKORANGE = "#723612"

    CANVAS_SIZE = 393, 600
    CELL_SIZE = 15
    ROWS, COLUMNS = (CANVAS_SIZE[0]//CELL_SIZE, CANVAS_SIZE[1]//CELL_SIZE)

    formatRC = lambda r,c: f"({r},{c})"
    flr = lambda id: id // Const.COLUMNS if id % Const.COLUMNS != 0 \
        or id == 0 else id // Const.COLUMNS - 1
    md = lambda id: id % Const.COLUMNS - 1 if id % Const.COLUMNS != 0 else Const.COLUMNS - 1

    options = ['fill', 'activefill', 'outline','tags']
    vals_alive = [ORANGE, ORANGE, WHITE, State.ALIVE]
    vals_dead = [LIGHT, DARKORANGE, ORANGE, State.DEAD]
    set_opts = lambda s: {k:v for k,v in zip(Const.options, Const.vals_dead)} if s == State.DEAD \
        else {k:v for k,v in zip(Const.options, Const.vals_alive)}