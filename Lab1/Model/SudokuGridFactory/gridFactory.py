import random
import time

import numpy

from Lab1.Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory
from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver
from Lab1.Model.SudokuSolver.sudokuSolver import SudokuSolver


class GridFactory(ISudokuGridFactory):
    __temp_grid: numpy.array
    __nums_list: numpy.array
    __length_of_block: int

    def __init__(self, length_of_block=3):
        self.__length_of_block = length_of_block

    def create_new_grid(self) -> numpy.array:
        self.__create_clear_grid()
        self.__fill_all_diagonal_boxes()
        print(self.__temp_grid)
        # ss: ISudokuSolver = SudokuSolver(self.__temp_grid)
        # return ss.get_solved_grid()

    def __create_clear_grid(self):
        side = self.__length_of_block ** 2
        self.__temp_grid = numpy.zeros((side, side), dtype=int)

    def __create_nums_list(self):
        nums = list(range(self.__length_of_block ** 2 + 1))
        nums.remove(0)
        random.shuffle(nums)
        self.__nums_list = numpy.array(nums, dtype=int)

    def __fill_all_diagonal_boxes(self):
        for i in range(self.__length_of_block):
            self.__create_nums_list()
            self.__fill_diagonal_box(i)

    def __fill_diagonal_box(self, index: int):
        start = index * self.__length_of_block
        for i in range(self.__length_of_block):
            for j in range(self.__length_of_block):
                self.__temp_grid[start + i][start + j] = self.__nums_list[i * self.__length_of_block + j]


gf = GridFactory(2)
gf.create_new_grid()