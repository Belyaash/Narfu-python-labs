from PyQt5.QtWidgets import QApplication

from Lab1.Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Lab1.Model.SudokuAppModel.sudokuAppModel import SudokuAppModel
from Lab1.ViewModel.ViewModel import ViewModel


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model: ISudokuAppModel = SudokuAppModel()
        self.view = ViewModel()
        self.view.setFixedSize(700, 500)
        self.view.set_model(self.model)
        self.view.select_difficulty_dialog()
