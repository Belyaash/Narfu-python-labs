from Lab1.Model.SudokuSolver.ISudokuSolver import ISudokuSolver


class SudokuSolver(ISudokuSolver):
    __grid: list[list[int]]
    __solutions = 0
    __row_of_unfilled_cell: int
    __col_of_unfilled_cell: int

    def __init__(self, unsolved_grid: list[list[int]]) -> None:
        self.__grid = unsolved_grid

    def set_grid(self, grid: list[list[int]]) -> None:
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
        self.__update_pos_of_unfilled_cell()
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
        self.__update_pos_of_unfilled_cell()
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
                    return False
        return True

    def __update_pos_of_unfilled_cell(self) -> None:
        for row in range(0, 9):
            for col in range(0, 9):
                if self.__grid[row][col] == 0:
                    self.__row_of_unfilled_cell = row
                    self.__col_of_unfilled_cell = col
                    return

    def __is_safe(self, grid, row, col, num) -> bool:
        if (self.__used_in_row(grid, row, num) is False) and (self.__used_in_column(grid, col, num) is False) and (
                self.__used_in_box(grid, row - row % 3, col - col % 3, num) is False):
            return True
        else:
            return False

    def __used_in_row(self, grid, row, num) -> bool:
        for i in range(9):
            if grid[row][i] == num:
                return True
        return False

    def __used_in_column(self, grid, col, num) -> bool:
        for i in range(9):
            if grid[i][col] == num:
                return True
        return False

    def __used_in_box(self, grid, row_start, col_start, num) -> bool:
        for i in range(3):
            for j in range(3):
                if grid[i + row_start][j + col_start] == num:
                    return True
        return False
