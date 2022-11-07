import time

import numpy

from Lab1.Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Lab1.Model.SudokuGameGridFactory.ISudokuGameGridFactory import ISudokuGameGridFactory
from Lab1.Model.SudokuGameGridFactory.sudokuGameGridFactory import SudokuGameGridFactory
from Lab1.Model.SudokuGridFactory.gridFactory import GridFactory
from Lab1.Model.cell import Cell
from Lab1.Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory


class SudokuAppModel(ISudokuAppModel):
    solved_grid: numpy.array
    game_grid: numpy.array
    solved_grid_factory: ISudokuGridFactory
    game_grid_factory: ISudokuGameGridFactory
    length_of_block: int
    level: int

    def __init__(self, length_of_block=3) -> None:
        self.level = 0
        self.length_of_block = length_of_block
        self.solved_grid_factory = GridFactory(length_of_block)
        self.game_grid_factory = SudokuGameGridFactory(30, length_of_block)

    def new_game(self) -> None:
        st = time.time()
        self.solved_grid = self.solved_grid_factory.create_new_grid()
        self.game_grid = self.game_grid_factory.create_game_grid(self.solved_grid)

    def is_player_win(self) -> bool:
        side = self.length_of_block ** 2
        for i in range(side):
            for j in range(side):
                if self.solved_grid[i][j] != self.game_grid[i][j].num:
                    return False
        return True

    def get_game_grid_cell_num(self, row, col) -> int:
        return self.game_grid[row][col].num

    def get_game_grid_cell_is_const(self, row, col) -> bool:
        return self.game_grid[row][col].isActive is False

    def get_solved_grid_cell(self, row, col) -> int:
        return self.solved_grid[row][col]

    def set_cell_num(self, row, col, num) -> None:
        self.game_grid[row][col].num = num

    def is_game_grid_filled(self) -> bool:
        side = self.length_of_block ** 2
        for i in range(side):
            for j in range(side):
                if self.game_grid[i][j].num == 0:
                    return False
        return True

    def set_length_of_block(self, length):
        self.length_of_block = length
        self.solved_grid_factory.set_length_of_block(length)
        self.game_grid_factory.set_length_of_block(length)
        self.set_difficulty(self.level)

    def set_difficulty(self, level: int) -> None:
        self.level = level
        self.game_grid_factory.difficulty = self.length_of_block**4 // (2.3 - 0.45*level)
