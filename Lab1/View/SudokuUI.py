# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SudokuUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(700, 500)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(15, 15, 470, 3))
        self.line.setAutoFillBackground(False)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(15, 172, 470, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(15, 327, 470, 3))
        self.line_3.setBaseSize(QtCore.QSize(2, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(15, 485, 470, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(15, 15, 3, 470))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(172, 15, 3, 470))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(328, 15, 3, 470))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(485, 15, 3, 470))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.newGameButton = QtWidgets.QPushButton(Form)
        self.newGameButton.setGeometry(QtCore.QRect(540, 15, 120, 30))
        self.newGameButton.setObjectName("newGameButton")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 460, 460))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.difficulty_label = QtWidgets.QLabel(Form)
        self.difficulty_label.setGeometry(QtCore.QRect(540, 60, 120, 30))
        self.difficulty_label.setText("Select difficulty")

        self.difficulty_combo_box = QtWidgets.QComboBox(Form)
        self.difficulty_combo_box.setGeometry(QtCore.QRect(540, 100, 120, 30))
        self.difficulty_combo_box.addItems(["Easy", "Medium", "Hard"])

        self.current_time_label = QtWidgets.QLabel(Form)
        self.current_time_label.setGeometry(QtCore.QRect(540, 150, 120, 30))
        self.current_time_label.setText("Current time")

        self.current_game_time = QtWidgets.QLabel(Form)
        self.current_game_time.setGeometry(QtCore.QRect(540, 170, 120, 30))
        self.current_game_time.setText("00:00:00")

        self.best_time_label = QtWidgets.QLabel(Form)
        self.best_time_label.setGeometry(QtCore.QRect(540, 230, 120, 30))
        self.best_time_label.setText("Best time")

        self.best_game_time = QtWidgets.QLabel(Form)
        self.best_game_time.setGeometry(QtCore.QRect(540, 250, 120, 30))
        self.best_game_time.setText("00:00:00")

        self.solve_button = QtWidgets.QPushButton(Form)
        self.solve_button.setGeometry(QtCore.QRect(540, 270, 120, 30))
        self.solve_button.setText("Solve")

        font = QFont('Century', 14)
        self.cells = []
        positions = [(i, j) for i in range(9) for j in range(9)]
        for position in positions:
            btn = QPushButton()
            btn.setMaximumSize(QtCore.QSize(50, 50))
            btn.setFont(font)
            self.gridLayout.addWidget(btn, *position)
            self.cells.append(btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SudokuMVC"))
        self.newGameButton.setText(_translate("Form", "Start New Game"))
