from PyQt5 import QtWidgets, QtCore

from Lab1.View.SelectDifficultyUI import SelectDifficulty
from Lab1.View.SudokuUI import Ui_Form
from Lab1.View.SetDigitsUI import Digits
from Lab1.Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Lab1.saver import Saver


class ViewModel(Ui_Form, QtWidgets.QMainWindow):
    __cells_value: list = None
    __const_cells: list = None
    __seconds: int = 0
    model: ISudokuAppModel = None
    timer: QtCore.QTimer = QtCore.QTimer()
    saver: Saver = Saver()

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(1000)
        self.newGameButton.clicked.connect(self.new_game)
        self.solve_button.clicked.connect(self.solve)
        self.difficulty_combo_box.currentTextChanged.connect(self.set_difficulty)
        for button in self.cells:
            button.clicked.connect(self.__cell_clicked)

    def set_model(self, model: ISudokuAppModel):
        self.model = model

    def new_game(self):
        """
        Create new game grid
        :return:
        """
        self.model.new_game()
        self.__refresh_grid()
        self.__refresh_game_menu()
        self.__set_button_style_and_text()

    def select_difficulty_dialog(self):
        self.close()
        select_diff = SelectDifficulty()
        select_diff.exec()
        self.difficulty_combo_box.setCurrentText(select_diff.difficulty_name)
        self.show()

    def __refresh_game_menu(self):
        self.timer.stop()
        self.__seconds = 0
        self.best_game_time.setText(self.saver.get_data(self.difficulty_combo_box.currentText()))
        self.current_game_time.setText("00:00:00")
        self.timer.start()

    def __refresh_grid(self):
        self.__cells_value = []
        self.__const_cells = []
        for i in range(9):
            for j in range(9):
                self.__cells_value.append(self.model.get_game_grid_cell_num(i, j))
                self.__const_cells.append(self.model.get_game_grid_cell_is_const(i, j))

    def __set_button_style_and_text(self):
        """
        Set game grid buttons style
        :return:
        """
        for i in range(len(self.cells)):
            button = self.cells[i]
            if self.__const_cells[i]:
                style = """
                           QPushButton { background-color: silver; }
                           QPushButton:pressed { background-color: red; }
                        """
                button.setText(str(self.__cells_value[i]))
            else:
                style = """
                           QPushButton { background-color: white; }
                           QPushButton:hover { background-color: gray; }
                        """
                button.setText("")
            button.setStyleSheet(style)

    def __cell_clicked(self):
        """
        Event for click on game grid button
        Try to set a num in grid
        If grid is full open Dialog with a player
        :return:
        """
        button = self.sender()
        index = self.cells.index(button)

        if self.__const_cells[index]:
            return

        digit = self.__get_user_digit()
        if not digit:
            return

        self.model.set_cell_num(index // 9, index % 9, int(digit))

        if digit == "0":
            digit = " "

        button.setText(digit)
        self.start_dialog_if_grid_full()

    @staticmethod
    def __get_user_digit():
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
                self.__win_dialog()
            else:
                self.__fail_dialog()

    def __win_dialog(self):
        """
        Win dialog
        :return:
        """
        win_dialog = QtWidgets.QMessageBox()
        win_dialog.setText("SudokuMVC is filled correctly/ Победа")
        win_dialog.setWindowTitle("Win")
        win_dialog.setIcon(QtWidgets.QMessageBox.Information)
        win_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.timer.stop()
        self.__try_update_best_time()
        win_dialog.exec_()


    def __fail_dialog(self):
        """
        Lose dialog
        :return:
        """
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setText("SudokuMVC is filled in incorrectly / Решение неверно")
        error_dialog.setWindowTitle("Fail")
        error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error_dialog.exec_()

    def set_difficulty(self, s):
        if s == "Easy":
            self.model.set_difficulty(0)
        if s == "Medium":
            self.model.set_difficulty(1)
        if s == "Hard":
            self.model.set_difficulty(2)
        self.new_game()

    def timer_tick(self):
        self.__seconds += 1
        self.current_game_time.setText(self.get_time())

    def get_time(self):
        hours = self.__seconds // 3600
        minutes = (self.__seconds - hours * 3600) // 60
        seconds = (self.__seconds - hours * 3600 - minutes * 60)

        return (self.__convert_int_to_time_presentation(hours) + ":"
                + self.__convert_int_to_time_presentation(minutes) + ":"
                + self.__convert_int_to_time_presentation(seconds))

    @staticmethod
    def __convert_int_to_time_presentation(time: int) -> str:
        if time < 10:
            return "0" + str(time)
        else:
            return str(time)

    def __try_update_best_time(self):
        best_time = self.saver.get_data(self.difficulty_combo_box.currentText()).split(':')
        best_time_seconds = int(best_time[0])*3600 + int(best_time[1])*60 + int(best_time[2])
        if (self.__seconds < best_time_seconds) or (best_time_seconds == 0):
            self.saver.save_data(self.difficulty_combo_box.currentText(), self.get_time())

    def solve(self):
        for i in range(81):
            correct_num = self.model.get_solved_grid_cell(i//9, i%9)
            self.model.set_cell_num(i // 9, i % 9, correct_num)
            button = self.cells[i]
            button.setText(str(correct_num))
        self.__win_dialog()
