import copy
import random

import numpy

from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver
from Lab1.Model.SudokuGameGridFactory.ISudokuGameGridFactory import ISudokuGameGridFactory
from Lab1.Model.cell import Cell
from Lab1.Model.SudokuSolver.sudokuSolver import SudokuSolver


class SudokuGameGridFactory(ISudokuGameGridFactory):
    difficulty: int
    game_grid: numpy.array
    __solved_grid: numpy.array
    __difficulty_of_game_grid: int
    __order_of_deletion: numpy.array

    def __init__(self, difficulty: int = 50) -> None:
        self.difficulty = difficulty

    def create_game_grid(self, grid) -> numpy.array:
        self.__solved_grid = grid
        self.__difficulty_of_game_grid = 0

        while self.__difficulty_of_game_grid < self.difficulty - 5:
            self.__difficulty_of_game_grid = 0
            self.__create_order_of_deletion()
            self.__create_game_matrix()

        return self.__convert_num_matrix_to_cell_matrix(self.game_grid)

    def __create_order_of_deletion(self) -> None:
        order = []
        for i in range(81):
            order.append(i)

        random.shuffle(order)
        self.__order_of_deletion = numpy.array(order, dtype=int)

    def __create_game_matrix(self) -> None:
        self.game_grid = copy.deepcopy(self.__solved_grid)
        sudoku_solver: ISudokuSolver = SudokuSolver(self.game_grid)
        for i in range(81):
            if self.__difficulty_of_game_grid >= self.difficulty + 2:
                break
            row = self.__order_of_deletion[i] // 9
            col = self.__order_of_deletion[i] % 9
            temp = self.game_grid[row][col]
            self.game_grid[row][col] = 0
            self.__difficulty_of_game_grid += 1
            if sudoku_solver.is_grid_have_only_one_solution() is False:
                self.game_grid[row][col] = temp
                self.__difficulty_of_game_grid -= 1

    @staticmethod
    def __convert_num_matrix_to_cell_matrix(grid) -> numpy.array:
        """
        convert matrix of ints to matrix of cells
        :param grid:
        :return: list[list[Cell]]
        """
        new_grid = []
        for i in grid:
            line = []
            for j in i:
                line.append(Cell(j))
            new_grid.append(line)

        return new_grid
