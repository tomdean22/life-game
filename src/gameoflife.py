import numpy as np
from .helpers import State, Trigger, Configuration as config


class Game:
    """
    A class for Conway's Game of Life
    
    Attributes:
        board: 2D numpy array of cells as (row, column) tuples
        rules: Conway's Game of Life rules    
    """
    rules = {
        State.DEAD: (Trigger.JUSTRIGHT, State.ALIVE),
        State.ALIVE: (Trigger.BADPOPULATION, State.DEAD)
    }

    def __init__(self, seed=None):
        """
        Create a new Game Board
        
        Parameters:
            seed: list of live cells as (row, column) tuples
        """
        self.initialize_board_from_seed(seed)

    def initialize_board_from_seed(self, seed:[(1,2),(3,4)]=None):
        """
        Create a 2D numpy array with an initial state of State.DEAD.
        Change state of cells in seed to State.ALIVE.

        Parameters;
            seed: list of live cells as (row, column) tuples
        """

        self.board = np.full((config.ROWS,config.COLUMNS), State.DEAD)
        if seed is None or len(seed) == 0:
            return
        else:
            print(f"[gameoflife.Game.initialize_board_from_seed]: {seed}")

        for r,c in seed:
            self.board[r][c] = State.ALIVE
        
    def count_neighbors(self, row, column) -> int:
        """
        Return the number of live cells surrounding self.board[row][column] 
        
        Parameters:
            row, column

        Returns:
            count: number of neighbors
        """
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
        """ Apply Conway's rules """

        next_gen = np.full((config.ROWS, config.COLUMNS), State.DEAD)
        for row in range(config.ROWS):
            for column in range(config.COLUMNS):
                state = self.board[row][column]
                if Game.rules[state][0](row, column, self):
                    print(f"[gameoflife.Game.update_board]: \
                        ({row:2},{column:2}) {state:1} -> {Game.rules[state][1]}")
                    next_gen[row][column] = Game.rules[state][1]
                else:
                    next_gen[row][column] = state
        del(self.board)
        self.board = next_gen

    def get_live_cells(self) -> list:
        """
        Gathers live cells for the display
        
        Returns:
            live_cells: list of live cells as (row, column) tuples
        """

        # Thought: keep board sorted according to value,
        #          so all State.ALIVE cells are grouped together.

        live_cells = []
        for row in range(config.ROWS):
            for column in range(config.COLUMNS):
                if self.board[row][column] == State.ALIVE:
                    live_cells.append((row,column))
        print(f"\n[gameoflife.Game.get_live_cells]: {live_cells}")
        return live_cells

