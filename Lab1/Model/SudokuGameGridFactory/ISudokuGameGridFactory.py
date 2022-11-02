from Lab1.Model.cell import Cell


class ISudokuGameGridFactory:
    difficulty: int
    game_grid: list[list[int]]

    def __init__(self, difficulty: int = 50) -> None:
        pass

    def create_game_grid(self, grid: list[list[int]]) -> list[list[Cell]]:
        pass
