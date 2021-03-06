# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.btnMin = QtGui.QPushButton("Collapse")
        self.btnMax = QtGui.QPushButton("Expand")
        self.btnFull = QtGui.QPushButton("Full Window")
        self.btnNormal = QtGui.QPushButton("Normal Size")
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btnMin)
        vbox.addWidget(self.btnMax)
        vbox.addWidget(self.btnFull)
        vbox.addWidget(self.btnNormal)
        self.setLayout(vbox)
        self.connect(self.btnMin, QtCore.SIGNAL("clicked()"),
                     self.on_min)
        self.connect(self.btnMax, QtCore.SIGNAL("clicked()"),
                     self.on_max)
        self.connect(self.btnFull, QtCore.SIGNAL("clicked()"),
                     self.on_full)
        self.connect(self.btnNormal, QtCore.SIGNAL("clicked()"),
                     self.on_normal)

        self.setWindowTitle("Expanding and minimizing the window")
        self.resize(300, 100)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()



if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtGui.QApplication(sys.argv)
    main = MyWindow()
    main.show()

    if app is not None:
        app.exec_()