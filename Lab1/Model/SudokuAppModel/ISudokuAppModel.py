import numpy

from Lab1.Model.SudokuGameGridFactory.ISudokuGameGridFactory import ISudokuGameGridFactory
from Lab1.Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory
from Lab1.Model.cell import Cell


class ISudokuAppModel:
    solved_grid: numpy.array
    game_grid: numpy.array
    solved_grid_factory: ISudokuGridFactory
    game_grid_factory: ISudokuGameGridFactory

    def __init__(self) -> None:
        pass

    def new_game(self) -> None:
        pass

    def is_player_win(self) -> bool:
        pass

    def get_game_grid_cell_num(self, row, col) -> int:
        pass

    def get_game_grid_cell_is_const(self, row, col) -> bool:
        pass

    def get_solved_grid_cell(self, row, col) -> int:
        pass

    def set_cell_num(self, row, col, num) -> None:
        pass

    def is_game_grid_filled(self) -> bool:
        pass

    def set_difficulty(self) -> None:
        pass
