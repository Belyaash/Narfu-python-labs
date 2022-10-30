from PyQt5 import QtWidgets

from GUI.SudokuUI import Ui_Form
from GUI.SetDigitsUI import Digits
from Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel


class MainWindow(Ui_Form, QtWidgets.QMainWindow):
    _cells_value: list = None
    _const_cells: list = None
    model: ISudokuAppModel = None

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.newGameButton.clicked.connect(self.new_game)
        self.difficulty_combo_box.currentTextChanged.connect(self.set_difficulty)
        self._button_bind()

    def _button_bind(self):
        """
        Bind events for game grid buttons
        :return:
        """
        for button in self.cells:
            button.clicked.connect(self._cell_clicked)

    def new_game(self):
        """
        Create new game grid
        :return:
        """
        self.model.new_game()
        self._cells_value = []
        self._const_cells = []
        for i in range(9):
            for j in range(9):
                self._cells_value.append(self.model.get_game_grid_cell_num(i, j))
                self._const_cells.append(self.model.get_game_grid_cell_is_const(i, j))

        self._set_button_style_and_text()

    def _set_button_style_and_text(self):
        """
        Set game grid buttons style
        :return:
        """
        for i in range(len(self.cells)):
            button = self.cells[i]
            if self._const_cells[i]:
                style = """
                           QPushButton { background-color: silver; }
                           QPushButton:pressed { background-color: red; }
                        """
                button.setText(str(self._cells_value[i]))
            else:
                style = """
                           QPushButton { background-color: white; }
                           QPushButton:hover { background-color: gray; }
                        """
                button.setText("")
            button.setStyleSheet(style)

    def _cell_clicked(self):
        """
        Event for click on game grid button
        Try to set a num in grid
        If grid is full open Dialog with a player
        :return:
        """
        button = self.sender()
        index = self.cells.index(button)

        if self._const_cells[index]:
            return

        digit = self._get_user_digit()
        if not digit:
            return

        self.model.set_cell_num(index // 9, index % 9, int(digit))

        if digit == "0":
            digit = " "

        button.setText(digit)
        self.start_dialog_if_grid_full()


    @staticmethod
    def _get_user_digit():
        """
        Open window for a digit choose
        :return:
        """
        window = Digits()
        window.exec()
        return window.num

    def start_dialog_if_grid_full(self):
        """
        Choose which one dialog will be open if game grid is full
        :return:
        """
        if self.model.is_game_grid_filled():
            if self.model.is_player_win():
                self._win()
            else:
                self._fail()

    def _win(self):
        """
        Win dialog
        :return:
        """
        win_dialog = QtWidgets.QErrorMessage(self)
        win_dialog.showMessage("SudokuMVC is filled correctly/ Победа")

    def _fail(self):
        """
        Lose dialog
        :return:
        """
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage("SudokuMVC is filled in incorrectly / Решение неверно")

    def set_model(self, model: ISudokuAppModel):
        self.model = model

    def set_difficulty(self, s):
        if s == "Easy":
            self.model.set_difficulty(35)
        if s == "Medium":
            self.model.set_difficulty(40)
        if s == "Hard":
            self.model.set_difficulty(48)
