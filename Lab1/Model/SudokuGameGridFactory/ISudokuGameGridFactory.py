from Model.cell import Cell


class ISudokuGameGridFactory:
    difficulty: int = None
    game_grid: list[list[int]] = None

    def __init__(self, difficulty: int = 50) -> None:
        pass

    def create_game_grid(self, grid: list[list[int]]) -> list[list[Cell]]:
        pass
