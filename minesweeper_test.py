import pytest
from minesweeper import Minesweeper

def test_create_minefield():
    minesweeper = Minesweeper(5, 3)
    minesweeper.create_minefield()

def test_set_bombs():
    minesweeper = Minesweeper(5, 3)
    minesweeper.set_bombs()

def test_set_values():
    minesweeper = Minesweeper(5, 3)
    minesweeper.set_values()

def test_nbors():
    minesweeper = Minesweeper(5, 3)
    minesweeper.vis = []  # Reset vis
    minesweeper.nbors(1, 1)

def test_check_over():
    minesweeper = Minesweeper(5, 3)
    minesweeper.values_of_bombs = [['M', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ']]
    assert minesweeper.check_over() == False

def test_show_bombs():
    minesweeper = Minesweeper(5, 3)
    minesweeper.show_bombs()
