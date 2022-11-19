from PyQt5.QtWidgets import QApplication

from Lab1.Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Lab1.Model.SudokuAppModel.sudokuAppModel import SudokuAppModel
from Lab1.ViewModel.MainViewModel import MainViewModel


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model: ISudokuAppModel = SudokuAppModel()
        self.view = MainViewModel(self.model)
        self.view.setFixedSize(700, 500)
