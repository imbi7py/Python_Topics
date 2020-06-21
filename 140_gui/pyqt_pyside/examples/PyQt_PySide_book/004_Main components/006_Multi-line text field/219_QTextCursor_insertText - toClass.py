# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QTextCursor")
        self.resize(500, 250)
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5")
        button = QtGui.QPushButton("Insert text")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()


    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.textCursor()
        cur.beginEditBlock()              # Начало блока
        cur.insertText("New Block 1\n")
        cur.insertText("New Block 2\n")
        cur.endEditBlock()                # Конец блока
        cur.joinPreviousEditBlock()       # Продолжение предыдущего блока
        cur.insertText("New Block 3\n")
        cur.endEditBlock()                # Конец блока
        self.textEdit.setTextCursor(cur)

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtGui.QApplication(sys.argv)
    main = SampleWindow()
    main.show()

    if app is not None:
        app.exec_()
