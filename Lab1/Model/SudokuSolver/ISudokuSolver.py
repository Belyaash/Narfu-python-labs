import numpy


class ISudokuSolver(object):
    def set_grid(self, grid: numpy.array) -> None:
        pass

    def get_solved_grid(self):
        pass

    def is_grid_have_only_one_solution(self) -> bool:
        pass
