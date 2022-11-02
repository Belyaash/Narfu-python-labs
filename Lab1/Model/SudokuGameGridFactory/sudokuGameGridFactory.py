import copy
import random

from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver
from Lab1.Model.SudokuGameGridFactory.ISudokuGameGridFactory import ISudokuGameGridFactory
from Lab1.Model.cell import Cell
from Lab1.Model.SudokuSolver.sudokuSolver import SudokuSolver


class SudokuGameGridFactory(ISudokuGameGridFactory):
    difficulty: int = None
    game_grid: list[list[int]] = None
    __solved_grid: list[list[int]] = None
    __difficulty_of_game_grid: int = None
    __order_of_deletion: list[int] = None

    def __init__(self, difficulty: int = 50) -> None:
        self.difficulty = difficulty

    def create_game_grid(self, grid) -> list[list[Cell]]:
        self.__solved_grid = grid
        self.__difficulty_of_game_grid = 0

        while self.__difficulty_of_game_grid < self.difficulty - 5:
            self.__difficulty_of_game_grid = 0
            self.__create_order_of_deletion()
            self.__create_game_matrix()

        return self.__convert_num_matrix_to_cell_matrix(self.game_grid)

    def __create_order_of_deletion(self) -> None:
        self.__order_of_deletion = []
        for i in range(81):
            self.__order_of_deletion.append(i)

        random.shuffle(self.__order_of_deletion)

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
    def __convert_num_matrix_to_cell_matrix(grid) -> list[list[Cell]]:
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
