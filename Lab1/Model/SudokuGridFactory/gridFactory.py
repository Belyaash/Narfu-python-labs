import random

from Lab1.Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory
from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver
from Lab1.Model.SudokuSolver.sudokuSolver import SudokuSolver


class GridFactory(ISudokuGridFactory):
    __temp_grid: list[list[int]] = None
    __nums_list: list[int] = None

    def create_new_grid(self) -> list[list[int]]:
        self.__create_clear_grid()
        self.__fill_all_diagonal_boxes()
        ss: ISudokuSolver = SudokuSolver(self.__temp_grid)
        return ss.get_solved_grid()

    def __create_clear_grid(self):
        self.__temp_grid = []
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(0)
            self.__temp_grid.append(temp)

    def __create_nums_list(self):
        self.__nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.__nums_list)

    def __fill_all_diagonal_boxes(self):
        for i in range(3):
            self.__create_nums_list()
            self.__fill_diagonal_box(i)

    def __fill_diagonal_box(self, index: int):
        start = index * 3
        for i in range(3):
            for j in range(3):
                self.__temp_grid[start + i][start + j] = self.__nums_list[i * 3 + j]