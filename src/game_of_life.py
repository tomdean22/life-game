from enum import Enum, auto
import numpy as np
from src.views import ROWS, COLUMNS


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
        self.initialize_board_from_seed(seed)

    def initialize_board_from_seed(self, seed=None):
        """ seed is a list of coordinate pairs representing cells (e.g. [(3,4),(5,6)]) """
        self.board = np.full((ROWS,COLUMNS), State.DEAD)
        if seed is None or len(seed) == 0:
            return

        print(f"\n[initialize]: {seed}, first: {seed[0]}")
        for r,c in seed:
            self.board[r][c] = State.ALIVE
        
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
                        # print(f"\n[IndexError]: ({row+i},{column+j})")
                        pass
        return count

    def update_board(self):
        print('\n')
        next_gen = np.full((ROWS, COLUMNS), State.DEAD)
        for row in range(ROWS):
            for column in range(COLUMNS):
                state = self.board[row][column]
                if Game.rules[state][0](row, column, self):
                    print(f"[update_board]: ({row}, {column}) {state} -> {Game.rules[state][1]}")
                    next_gen[row][column] = Game.rules[state][1]
                else:
                    next_gen[row][column] = state
        del(self.board)
        self.board = next_gen

    def get_live_cells(self):
        alive = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] == State.ALIVE:
                    alive.append((row,column))
        print(f"\n[get_live_cells]: {alive}")
        return alive

