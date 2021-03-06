# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys


class AddItems(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        L = []
        for i in range(1, 11):
            L.append("Пункт {0}".format(i))
        self.comboBox.addItems(L)
        button = QtWidgets.QPushButton("Получить значение")
        button.clicked.connect(self.on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print("Текст:", self.comboBox.currentText())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = AddItems()
    sys.exit(app.exec_())