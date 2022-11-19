import sys

from PyQt5 import QtWidgets, QtCore

from Lab1.View.SelectDifficultyUI import SelectDifficulty
from Lab1.View.SudokuUI import Ui_Form
from Lab1.View.SetDigitsUI import Digits
from Lab1.Model.SudokuAppModel.ISudokuAppModel import ISudokuAppModel
from Lab1.saver import Saver


class MainViewModel(Ui_Form, QtWidgets.QMainWindow):
    __cells_value: list = []
    __const_cells: list = []
    __seconds: int = 0
    model: ISudokuAppModel
    timer: QtCore.QTimer = QtCore.QTimer()
    saver: Saver = Saver()
    length_of_block: int
    difficulty_level: int

    def __init__(self, model: ISudokuAppModel, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.model = model
        self.timer.timeout.connect(self.timer_tick)
        self.timer.setInterval(1000)
        self.newGameButton.clicked.connect(self.start_new_game)
        self.solve_button.clicked.connect(self.solve)

        self.select_difficulty_dialog()
        self.start_new_game()

    def select_difficulty_dialog(self):
        self.close()
        select_diff = SelectDifficulty()
        select_diff.exec()
        try:
            self.difficulty_combo_box.setCurrentText(select_diff.difficulty_name)
            self.size_cb.setCurrentText(select_diff.length_name)
            self.show()
        except:
            sys.exit()

    def start_new_game(self):
        self.set_difficulty(self.difficulty_combo_box.currentText())
        self.set_length_of_block(self.size_cb.currentText())
        self.createGrid(self, self.length_of_block)
        for button in self.cells:
            button.clicked.connect(self.__cell_clicked)
        self.model.new_game()
        self.__refresh_grid()
        self.__refresh_game_menu()
        self.__set_button_style_and_text()

    def set_difficulty(self, s: str):
        if s == "Easy":
            self.difficulty_level = 0
        if s == "Medium":
            self.difficulty_level = 1
        if s == "Hard":
            self.difficulty_level = 2
        self.model.set_difficulty(self.difficulty_level)

    def set_length_of_block(self, s: str):
        self.length_of_block = int(s[0])
        self.model.set_length_of_block(self.length_of_block)

    def __refresh_grid(self):
        self.__cells_value = []
        self.__const_cells = []
        side = self.length_of_block ** 2
        for i in range(side):
            for j in range(side):
                self.__cells_value.append(self.model.get_game_grid_cell_num(i, j))
                self.__const_cells.append(self.model.get_game_grid_cell_is_const(i, j))

    def __refresh_game_menu(self):
        self.timer.stop()
        self.__seconds = 0
        str_to_saver = self.__get_str_to_saver()
        self.best_game_time.setText(self.saver.get_data(str_to_saver))
        self.current_game_time.setText("00:00:00")
        self.condition.setText(" ")
        self.condition.setStyleSheet("QLabel { background-color : #f0f0f0; }")
        self.timer.start()

    def __set_button_style_and_text(self):
        for i in range(len(self.cells)):
            button = self.cells[i]
            if self.__const_cells[i]:
                style = """
                           QPushButton {color: blue}
                           QPushButton:pressed { background-color: red; }
                        """
                button.setText(str(self.__cells_value[i]))
            else:
                style = """
                           QPushButton { background-color: white; border: 1px solid gray}
                           QPushButton:hover { border: 2px solid blue; }
                        """
                button.setText("")
            button.setStyleSheet(style)

    def __cell_clicked(self):
        button = self.sender()
        index = self.cells.index(button)

        if self.__const_cells[index]:
            return

        digit = self.__set_digit_dialog()
        if not digit:
            return

        side = self.length_of_block**2
        self.model.set_cell_num(index // side, index % side, int(digit))

        if digit == "0":
            digit = " "

        button.setText(digit)
        self.stop_game_if_grid_filled_correct()

    def __set_digit_dialog(self):
        window = Digits(self.length_of_block)
        window.exec()
        return window.num

    def stop_game_if_grid_filled_correct(self):
        if self.model.is_game_grid_filled():
            if self.model.is_player_win():
                self.condition.setText("Sudoku is filled correctly")
                self.condition.setStyleSheet("QLabel { background-color : green; color : blue; }")
                self.__const_cells = list(range(self.length_of_block**4))
                self.timer.stop()
                self.__try_update_best_time()
            else:
                self.condition.setText("  You have some errors")
                self.condition.setStyleSheet("QLabel { background-color : red; color : blue; }")
        else:
            self.condition.setText(" ")
            self.condition.setStyleSheet("QLabel { background-color : #f0f0f0; color : blue; }")

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
        str_to_saver = self.__get_str_to_saver()
        best_time = self.saver.get_data(str_to_saver).split(':')
        best_time_seconds = int(best_time[0])*3600 + int(best_time[1])*60 + int(best_time[2])
        if (self.__seconds < best_time_seconds) or (best_time_seconds == 0):
            self.saver.save_data(str_to_saver, self.get_time())
            self.best_game_time.setText(self.current_game_time.text())

    def __get_str_to_saver(self) -> str:
        return str(self.length_of_block) + str(self.difficulty_level)

    def solve(self):
        side = self.length_of_block**2
        for i in range(side**2):
            correct_num = self.model.get_solved_grid_cell(i//side, i%side)
            self.model.set_cell_num(i // side, i % side, correct_num)
            button = self.cells[i]
            button.setText(str(correct_num))
        self.stop_game_if_grid_filled_correct()
