# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 80)
button1 = QtGui.QPushButton("Кнопка 1")
button2 = QtGui.QPushButton("Кнопка 2")
button1.setCheckable(True)
button2.setCheckable(True)
button1.setAutoExclusive(True)
button2.setAutoExclusive(True)
mainbox = QtGui.QVBoxLayout()
box = QtGui.QGroupBox("Группа кнопок-переключателей")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
button1.setChecked(True)
window.show()
sys.exit(app.exec_())