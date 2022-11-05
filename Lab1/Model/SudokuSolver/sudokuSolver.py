import numpy

from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver


class SudokuSolver(ISudokuSolver):
    __grid: numpy.array
    __solutions = 0
    __row_of_unfilled_cell: int
    __col_of_unfilled_cell: int

    def __init__(self, solved_grid: numpy.array) -> None:
        self.set_grid(solved_grid)

    def set_grid(self, grid: numpy.array) -> None:
        self.__grid = grid

    def get_solved_grid(self):
        self.__solve_grid()
        return self.__grid

    def is_grid_have_only_one_solution(self) -> bool:
        self.__solutions = 0
        self.__count_solutions()
        return self.__solutions == 1

    def __solve_grid(self) -> bool:
        if self.__is_grid_filled():
            return True
        row = self.__row_of_unfilled_cell
        col = self.__col_of_unfilled_cell
        for i in range(1, 10):
            if self.__is_safe(self.__grid, row, col, i):
                self.__grid[row][col] = i
                if self.__solve_grid():
                    return True
                self.__grid[row][col] = 0
        return False

    def __count_solutions(self) -> None:
        if self.__is_grid_filled():
            self.__solutions += 1
            return
        row = self.__row_of_unfilled_cell
        col = self.__col_of_unfilled_cell
        for i in range(1, 10):
            if self.__solutions > 1:
                return
            if self.__is_safe(self.__grid, row, col, i):
                self.__grid[row][col] = i
                self.__count_solutions()
            self.__grid[row][col] = 0

    def __is_grid_filled(self) -> bool:
        """
        A function to check if the grid is full
        :return: bool
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if self.__grid[row][col] == 0:
                    self.__row_of_unfilled_cell = row
                    self.__col_of_unfilled_cell = col
                    return False
        return True

    def __is_safe(self, grid, row, col, num) -> bool:
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(9):
            if (grid[row][i] == num) or (grid[i][col] == num) or (grid[i//3 + start_row][i%3 + start_col] == num):
                return False
        return True

