import numpy as np
from .helpers import State, Trigger, Config as cnf


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
            seed: list of live cells as cell ids
        """
        self.board = np.full((cnf.ROWS,cnf.COLUMNS), State.DEAD)
        self.initialize_board_from_seed(seed)

    def initialize_board_from_seed(self, seed:(1,2,3)=None):
        """
        Create a 2D numpy array with an initial state of State.DEAD.
        Change state of cells in seed to State.ALIVE.

        Parameters;
            seed: list of live cells as cell ids
        """
        
        del(self.board)
        self.board = np.full((cnf.ROWS,cnf.COLUMNS), State.DEAD)
        
        if seed is None or len(seed) == 0:
            return

        print(f"[gameoflife.Game.initialize_board_from_seed]: {seed}")
        for r,c in map(cnf.convertIDtoRC, seed):
            self.board[r,c] = State.ALIVE

    def reset_board(self):
        self.initialize_board_from_seed(seed=None)
        
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
                        if self.board[row+i, column+j] is State.ALIVE:
                            count += 1
                    except IndexError:
                        # What to do with neighbor cells outside the grid?
                        # print(f"\n[IndexError]: ({row+i},{column+j})")
                        pass
        return count

    def update_board(self):
        """ Apply Conway's rules """

        next_gen = np.full((cnf.ROWS, cnf.COLUMNS), State.DEAD)

        for i,row in enumerate(self.board):
            for j,cell_state in enumerate(row):
                if Game.rules[cell_state][0](i,j,self):
                    print(f"[gameoflife.Game.update_board]: ({i:2},{j:2}) {cell_state:11} -> {Game.rules[cell_state][1]}")
                    next_gen[i,j] = Game.rules[cell_state][1]
                else:
                    next_gen[i,j] = cell_state
        del(self.board)
        self.board = next_gen

    def get_live_cells(self) -> list:
        """
        Gathers live cells for the display
        
        Returns:
            live_cells: list of live cells as (row, column) tuples
        """

        # numpy arrays return an array of booleans when checking for equality
        linear_pos = 1
        live_cells = []
        for row in self.board == State.ALIVE:
            for column in row:
                if column:
                    live_cells.append(linear_pos)
                linear_pos += 1
        print(f"[gameoflife.Game.get_live_cells]: {live_cells}")
        return live_cells
