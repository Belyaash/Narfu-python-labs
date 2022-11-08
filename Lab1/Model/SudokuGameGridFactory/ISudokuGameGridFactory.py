import numpy

from Lab1.Model.cell import Cell


class ISudokuGameGridFactory:
    difficulty: int
    game_grid: numpy.array

    def __init__(self, difficulty: int = 50) -> None:
        pass

    def create_game_grid(self, grid: numpy.array) -> numpy.array:
        pass

    def set_length_of_block(self, length):
        pass