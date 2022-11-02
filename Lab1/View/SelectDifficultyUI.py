from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel
from PyQt5 import QtCore

from Lab1.saver import Saver


class SelectDifficulty(QDialog):
    difficulty: int
    difficulty_name: str


    def __init__(self, *args):
        super().__init__(*args)
        self.difficulty = 0
        self.difficulty_name = ""
        self.setWindowTitle('Select a difficulty')
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()
        saver = Saver()

        label_easy = QLabel()
        label_easy.setGeometry(QtCore.QRect(0, 0, 60, 30))
        label_easy.setText("Easy")
        main_layout.addWidget(label_easy)

        best_time_easy = QLabel()
        best_time_easy.setGeometry(QtCore.QRect(0, 30, 60, 30))
        best_time_easy.setText(saver.get_data("Easy"))
        main_layout.addWidget(best_time_easy)

        label_medium = QLabel()
        label_medium.setGeometry(QtCore.QRect(0, 80, 60, 30))
        label_medium.setText("Medium")
        main_layout.addWidget(label_medium)

        best_time_medium = QLabel()
        best_time_medium.setGeometry(QtCore.QRect(0, 110, 60, 30))
        best_time_medium.setText(saver.get_data("Medium"))
        main_layout.addWidget(best_time_medium)

        label_hard = QLabel()
        label_hard.setGeometry(QtCore.QRect(0, 150, 60, 30))
        label_hard.setText("Hard")
        main_layout.addWidget(label_hard)

        best_time_hard = QLabel()
        best_time_hard.setGeometry(QtCore.QRect(0, 180, 60, 30))
        best_time_hard.setText(saver.get_data("Hard"))
        main_layout.addWidget(best_time_hard)

        easy_button = QPushButton()
        easy_button.setText("Select Easy")
        easy_button.clicked.connect(self.on_click_easy)
        main_layout.addWidget(easy_button, 0, 1, 2, 1)

        medium_button = QPushButton()
        medium_button.setText("Select Medium")
        medium_button.clicked.connect(self.on_click_medium)
        main_layout.addWidget(medium_button, 2, 1, 2, 1)

        hard_button = QPushButton()
        hard_button.setText("Select Hard")
        hard_button.clicked.connect(self.on_click_hard)
        main_layout.addWidget(hard_button, 4, 1, 2, 1)

        self.setLayout(main_layout)



    def on_click_easy(self):
        self.difficulty_name = "Easy"
        self.difficulty = 0
        self.close()

    def on_click_medium(self):
        self.difficulty_name = "Medium"
        self.difficulty = 1
        self.close()

    def on_click_hard(self):
        self.difficulty_name = "Hard"
        self.difficulty = 2
        self.close()
