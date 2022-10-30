import random

from Model.SudokuGridFactory.ISudokuGridFactory import ISudokuGridFactory


class SudokuGridFactory(ISudokuGridFactory):
    __solved_grid: list[list[int]] = None

    def __init__(self):
        self.__new_solved_grid()

    def create_new_grid(self) -> list[list[int]]:
        self.__shuffle_sudoku_grid()
        return self.__solved_grid

    def __new_solved_grid(self) -> None:
        self.__solved_grid = [[7, 1, 5, 3, 9, 8, 4, 6, 2],
                              [8, 2, 6, 5, 1, 4, 9, 7, 3],
                              [3, 9, 4, 2, 7, 6, 5, 8, 1],
                              [1, 8, 2, 9, 4, 3, 7, 5, 6],
                              [6, 4, 3, 7, 5, 1, 2, 9, 8],
                              [9, 5, 7, 8, 6, 2, 1, 3, 4],
                              [5, 6, 8, 1, 2, 7, 3, 4, 9],
                              [4, 7, 1, 6, 3, 9, 8, 2, 5],
                              [2, 3, 9, 4, 8, 5, 6, 1, 7]]

    def __shuffle_sudoku_grid(self, shuffles: int = 100) -> None:
        mix_func = ['self._transposing()',
                    'self._swap_rows_small()',
                    'self._swap_columns_small()',
                    'self._swap_rows_area()',
                    'self._swap_columns_area()']

        for i in range(shuffles):
            func = random.randint(0, len(mix_func) - 1)
            eval(mix_func[func])

    def _transposing(self) -> None:
        self.__solved_grid = list(map(list, zip(*self.__solved_grid)))

    def _swap_rows_small(self) -> None:
        area = random.randint(0, 2)
        line_of_area1 = random.randint(0, 2)
        line_of_area2 = random.randint(0, 2)

        while line_of_area1 == line_of_area2:
            line_of_area2 = random.randint(0, 2)

        line1 = line_of_area1 + area * 3
        line2 = line_of_area2 + area * 3

        self.__solved_grid[line1], self.__solved_grid[line2] = self.__solved_grid[line2], self.__solved_grid[line1]

    def _swap_columns_small(self) -> None:
        self._transposing()
        self._swap_rows_small()
        self._transposing()

    def _swap_rows_area(self) -> None:
        area1 = random.randint(0, 2)
        area2 = random.randint(0, 2)

        while area1 == area2:
            area2 = random.randint(0, 2)

        for i in range(3):
            line1 = i + area1 * 3
            line2 = i + area2 * 3
            self.__solved_grid[line1], self.__solved_grid[line2] = self.__solved_grid[line2], self.__solved_grid[line1]

    def _swap_columns_area(self) -> None:
        self._transposing()
        self._swap_rows_area()
        self._transposing()