import pytest
from minesweeper import Minesweeper

def test_create_minefield():
    # Создаем экземпляр Minesweeper с полем 5x3
    minesweeper = Minesweeper(5, 3)
    
    # Вызываем метод create_minefield для генерации поля с минами
    minesweeper.create_minefield()
    
    # Проверяем, что метод create_minefield выводит что-то в консоль
    # В данном случае, мы просто проверяем, что не выбрасывается исключение при его вызове
    try:
        minesweeper.create_minefield()
    except Exception as e:
        assert False, f"An unexpected exception occurred: {e}"
        
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

    # После выполнения nbors, ожидается, что в vis будут все посещенные ячейки
    expected_visited_cells = [[1, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
    
    # Проверяем, что все посещенные ячейки присутствуют в vis
    for cell in expected_visited_cells:
        assert cell in minesweeper.vis

def test_check_over():
    minesweeper = Minesweeper(5, 3)
    minesweeper.values_of_bombs = [['M', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' '],
                                   [' ', ' ', ' ', ' ', ' ']]
    assert minesweeper.check_over() == False
