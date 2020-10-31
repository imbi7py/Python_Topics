# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys


class SetCompleter(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Класс QComboBox")
        self.resize(300, 90)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        arr = ["кадр", "каменный", "камень", "камера"]
        completer = QtWidgets.QCompleter(arr, self)
        self.comboBox.setCompleter(completer)
        for i in range(1, 11):
            self.comboBox.addItem("Пункт {0}".format(i))
        button = QtWidgets.QPushButton("Получить индекс текущего элемента")
        button.clicked.connect(on_clicked)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.comboBox)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked():
        print(self.comboBox.currentIndex())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetCompleter()
    sys.exit(app.exec_())
