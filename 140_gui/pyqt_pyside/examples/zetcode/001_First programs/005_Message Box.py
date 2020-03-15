"""
ZetCode PyQt4 tutorial 

This program shows a confirmation 
message box when we click on the close
button of the application window. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PySide2.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QMessageBox.Yes |
                                           QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = Example()
    main.show()

    if app is not None:
        app.exec_()