from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton
from PyQt5 import QtCore


class Digits(QDialog):
    def __init__(self, *args):
        super().__init__(*args)
        self.num = None
        self.setWindowTitle('Select a num')
        self.__digits = "123456789"
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()
        font = QFont('Century', 14)

        positions = [(i, j) for i in range(3) for j in range(3)]

        for position, letter in zip(positions, self.__digits):
            btn = QPushButton(letter)
            btn.setFont(font)
            btn.clicked.connect(self.on_click)
            btn.setMaximumSize(QtCore.QSize(40, 40))
            main_layout.addWidget(btn, *position)

        empty_button = QPushButton()
        empty_button.setText("Empty")
        empty_button.setFont(font)
        empty_button.clicked.connect(self.on_click_empty)
        empty_button.setMaximumSize(QtCore.QSize(140, 40))
        main_layout.addWidget(empty_button, 3, 0, 3, 0)

        self.setLayout(main_layout)

    def on_click(self):
        btn = self.sender()
        self.num = btn.text()
        self.close()

    def on_click_empty(self):
        self.num = '0'
        self.close()
