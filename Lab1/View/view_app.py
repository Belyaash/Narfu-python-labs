from PyQt5.QtWidgets import QApplication

from Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Model.SudokuAppModel.sudokuAppModel import SudokuAppModel
from View.main_window import MainWindow


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model: ISudokuAppModel = SudokuAppModel()
        self.view = MainWindow()
        self.view.set_model(self.model)

        self.view.show()
