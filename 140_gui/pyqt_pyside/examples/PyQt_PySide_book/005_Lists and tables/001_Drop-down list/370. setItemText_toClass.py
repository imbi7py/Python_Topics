# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import sys


class SetItemText(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

def on_clicked():
    print("Текст:", comboBox.currentText())
    print("Данные:", comboBox.itemData(comboBox.currentIndex()))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
comboBox.setItemText(0, "Новое значение")
ico = window.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
comboBox.setItemIcon(0, ico)
comboBox.setItemData(0, 50, role=QtCore.Qt.UserRole)
comboBox.setItemData(0, "Это текст всплывающей подсказки",
                     role=QtCore.Qt.ToolTipRole)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SetItemText()
    sys.exit(app.exec_())