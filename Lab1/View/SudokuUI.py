from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(700, 500)

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
        self.difficulty_combo_box.setGeometry(QtCore.QRect(540, 90, 120, 30))
        self.difficulty_combo_box.addItems(["Easy", "Medium", "Hard"])

        self.size_label = QtWidgets.QLabel(Form)
        self.size_label.setGeometry(QtCore.QRect(540, 120, 120, 30))
        self.size_label.setText("Select block")

        self.size_cb = QtWidgets.QComboBox(Form)
        self.size_cb.setGeometry(QtCore.QRect(540, 150, 120, 30))
        self.size_cb.addItems(["2*2", "3*3"])

        self.current_time_label = QtWidgets.QLabel(Form)
        self.current_time_label.setGeometry(QtCore.QRect(540, 200, 120, 30))
        self.current_time_label.setText("Current time")

        self.current_game_time = QtWidgets.QLabel(Form)
        self.current_game_time.setGeometry(QtCore.QRect(540, 220, 120, 30))
        self.current_game_time.setText("00:00:00")

        self.best_time_label = QtWidgets.QLabel(Form)
        self.best_time_label.setGeometry(QtCore.QRect(540, 280, 120, 30))
        self.best_time_label.setText("Best time")

        self.best_game_time = QtWidgets.QLabel(Form)
        self.best_game_time.setGeometry(QtCore.QRect(540, 300, 120, 30))
        self.best_game_time.setText("00:00:00")

        self.solve_button = QtWidgets.QPushButton(Form)
        self.solve_button.setGeometry(QtCore.QRect(540, 350, 120, 30))
        self.solve_button.setText("Solve")

        self.condition = QtWidgets.QLabel(Form)
        self.condition.setGeometry(QtCore.QRect(530, 400, 140, 30))

        font = QFont('Century', 14)
        self.cells = []
        self.lines = []
        self.createGrid(Form)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SudokuMVC"))
        self.newGameButton.setText(_translate("Form", "Start New Game"))

    def createGrid(self, Form, num_of_blocks_in_line=3):
        for line in self.lines:
            line.close()
        for cell in self.cells:
            cell.close()
        self.cells.clear()
        self.lines = []
        for i in range(num_of_blocks_in_line+1):
            line = QtWidgets.QFrame(Form)
            line.setGeometry(QtCore.QRect(15, 15 + i * (470//num_of_blocks_in_line),470, 3))
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.lines.append(line)
            line.show()
            line = QtWidgets.QFrame(Form)
            line.setGeometry(QtCore.QRect(15 + i * (470 // num_of_blocks_in_line), 15, 3, 470))
            line.setFrameShape(QtWidgets.QFrame.VLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.show()
            self.lines.append(line)
        font = QFont('Century', 50//num_of_blocks_in_line)
        full_side = num_of_blocks_in_line**2
        positions = [(i, j) for i in range(full_side) for j in range(full_side)]
        for position in positions:
            btn = QPushButton()
            btn.setMaximumSize(QtCore.QSize(450//full_side, 450//full_side))
            btn.setFont(font)
            self.gridLayout.addWidget(btn, *position)
            self.cells.append(btn)