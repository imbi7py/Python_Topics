from PySide.QtGui import *

class dialogClass(QDialog):
    def __init__(self):
        super(dialogClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.label = QLineEdit()
        self.ly.addWidget(self.label)

        self.ok_btn = QPushButton('OK')
        self.ly.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton('Cancel')
        self.ly.addWidget(self.cancel_btn)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def getData(self):
        return dict(text=self.label.text())

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        self.dial = dialogClass()
        r = self.dial.exec_()
        if r:
            print self.dial.getData()

def main():
    global c
    c = simpleWindow()
    c.raise_()
    c.show()

main()