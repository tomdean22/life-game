import pytest
from tests.shapes import *
from src.game_of_life import Game

# === TEST NEIGHBOR COUNT ===

def checkNeighborCount( seed, row, column, expected_result):
    game = Game(seed)
    ret_val = game.count_neighbors(row, column)
    assert ret_val == expected_result

def test_GoodNeighborCountBLINKER():
    checkNeighborCount( BLINKER1, 5, 5, 2 ) # middle
    checkNeighborCount( BLINKER1, 5, 4, 1 ) # left
    checkNeighborCount( BLINKER1, 5, 6, 1 ) # right


# === TEST UPDATES FOR WELL-KNOWN PATTERNS ===

def checkUpdate( seed, expected_result ):
    game = Game(seed)
    game.update_board()
    ret_val = game.get_live_cells()
    assert ret_val == expected_result

def test_GoodSecondGenBlinker():
    checkUpdate( BLINKER1, BLINKER2 )

def test_GoodSecondGenToad():
    checkUpdate( TOAD1, TOAD2 )

def test_GoodSecondGenBeacon():
    checkUpdate( BEACON1, BEACON2 )