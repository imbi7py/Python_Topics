from PySide import QtGui, QtCore
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("addSpacing")
        self.resize(350, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addSpacing(100)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        self.setLayout(hbox)


def main():
    global c
    c = MyWindow()
    c.show()

main()