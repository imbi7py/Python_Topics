# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("setLabelAlignment")
window.resize(300, 150)
lineEdit = QtGui.QLineEdit()
textEdit = QtGui.QTextEdit()
spinBox = QtGui.QSpinBox()
button1 = QtGui.QPushButton("О&тправить")
button2 = QtGui.QPushButton("О&чистить")
hbox = QtGui.QHBoxLayout()
hbox.addWidget(button1)
hbox.addWidget(button2)
form = QtGui.QFormLayout()
form.setLabelAlignment(QtCore.Qt.AlignRight)
form.addRow("&Название:", lineEdit)
form.addRow("&Описание:", textEdit)
form.addRow("&Количество:", spinBox)
form.addRow(hbox)
window.setLayout(form)
window.show()
sys.exit(app.exec_())