from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.setWindowTitle("Класс QTabWidget")
        self.resize(300, 120)
        tab = QtGui.QTabWidget()
        tab.addTab(QtGui.QLabel("Содержимое вкладки 1"), "Вкладка &1")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 2"), "Вкладка &2")
        tab.addTab(QtGui.QLabel("Содержимое вкладки 3"), "Вкладка &3")
        tab.setCurrentIndex(0)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
