from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel
from PyQt5 import QtCore

from Lab1.saver import Saver


class SelectDifficulty(QDialog):
    difficulty_name: str
    length_name: str


    def __init__(self, *args):
        super().__init__(*args)
        self.difficulty_name = ""
        self.length_name = 3
        self.setWindowTitle('Select a difficulty')
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()
        self.saver = Saver()

        difficulty_label = QLabel()
        difficulty_label.setGeometry(QtCore.QRect(0, 0, 120, 30))
        difficulty_label.setText("Select difficulty")
        main_layout.addWidget(difficulty_label)

        self.difficulty_combo_box = QtWidgets.QComboBox()
        self.difficulty_combo_box.setGeometry(QtCore.QRect(0, 30, 120, 30))
        self.difficulty_combo_box.addItems(["Easy", "Medium", "Hard"])
        self.difficulty_combo_box.currentTextChanged.connect(self.update_time)
        main_layout.addWidget(self.difficulty_combo_box)

        size_label = QLabel()
        size_label.setGeometry(QtCore.QRect(0, 70, 120, 30))
        size_label.setText("Select block")
        main_layout.addWidget(size_label)

        self.size_cb = QtWidgets.QComboBox()
        self.size_cb.setGeometry(QtCore.QRect(0, 100, 120, 30))
        self.size_cb.addItems(["2*2", "3*3"])
        self.size_cb.setCurrentText("3*3")
        self.size_cb.currentTextChanged.connect(self.update_time)
        main_layout.addWidget(self.size_cb)

        best_time_label = QLabel()
        best_time_label.setGeometry(QtCore.QRect(0, 140, 120, 30))
        best_time_label.setText("Best time")
        main_layout.addWidget(best_time_label)

        self.best_game_time = QLabel()
        self.best_game_time.setGeometry(QtCore.QRect(0, 170, 120, 30))
        self.best_game_time.setText("00:00:00")
        main_layout.addWidget(self.best_game_time)
        self.update_time()

        select_button = QPushButton()
        select_button.setText("Select")
        select_button.clicked.connect(self.on_click)
        main_layout.addWidget(select_button)

        self.setLayout(main_layout)

    def on_click(self):
        self.difficulty_name = self.difficulty_combo_box.currentText()
        self.length_name = self.size_cb.currentText()
        self.close()

    def update_time(self):
        str_to_saver = self.difficulty_combo_box.currentText()+self.size_cb.currentText()
        self.best_game_time.setText(self.saver.get_data(str_to_saver))