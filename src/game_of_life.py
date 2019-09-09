from enum import Enum, auto
import numpy as np

ROWS, COLUMNS = 10, 10

class State(Enum):
    DEAD = auto()
    ALIVE = auto()


class Trigger(Enum):
    JUSTRIGHT     = lambda i,j,g: g.count_neighbors(i,j) == 3
    BADPOPULATION = lambda i,j,g: g.count_neighbors(i,j) < 2 or g.count_neighbors(i,j) > 3


class Game:
    rules = {
        State.DEAD: (Trigger.JUSTRIGHT, State.ALIVE),
        State.ALIVE: (Trigger.BADPOPULATION, State.DEAD)
    }

    def __init__(self, seed=None):
        self.board = Game.initialize_board_from_seed(seed)

    @staticmethod
    def initialize_board_from_seed(seed=None):
        """ seed is a list of coordinate pairs representing cells (e.g. [(3,4),(5,6)]) """
        board = np.full((ROWS,COLUMNS), State.DEAD)
        if seed is None:
            return board
            
        for r,c in seed:
            board[r][c] = State.ALIVE
        return board

    def count_neighbors(self, row, column):
        count = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i is 0 and j is 0:
                    pass
                else:
                    try:
                        if self.board[row+i][column+j] == State.ALIVE:
                            count += 1
                    except IndexError:
                        # What to do with neighbor cells outside the grid?
                        pass
        return count

    def update_board(self):
        next_gen = np.full((ROWS, COLUMNS), State.DEAD)
        for row in range(ROWS):
            for column in range(COLUMNS):
                state = self.board[row][column]
                if Game.rules[state][0](row, column, self):
                    next_gen[row][column] = Game.rules[state][1]
                else:
                    next_gen[row][column] = state
        self.board = next_gen

    def get_live_cells(self):
        alive = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] == State.ALIVE:
                    alive.append((row,column))
        return alive

