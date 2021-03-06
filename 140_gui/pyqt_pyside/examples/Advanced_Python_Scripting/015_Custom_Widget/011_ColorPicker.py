from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class pickerClass(QWidget):
    def __init__(self):
        super(pickerClass, self).__init__()
        self.sz = 300
        self.setFixedSize(QSize(self.sz, self.sz))
        self.img = self.getRamp()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rec = event.rect()
        painter.drawImage(0, 0, self.img)
        painter.end()

    def getRamp(self):
        img = QImage(self.sz, self.sz, QImage.Format_RGB32)
        color = QColor()
        for x in range(self.sz):
            h = x / float(self.sz)
            for y in range(self.sz):
                s = y / float(self.sz)
                v = 1
                color.setHsvF(h, s, v)
                img.setPixel(x, y, color.rgb())
        return img

    def mousePressEvent(self, event):
        super(pickerClass, self).mousePressEvent(event)
        self.getColor(event.pos())

    def getColor(self, pos):
        # print pos
        h = pos.x()/float(self.sz)
        s = pos.y()/float(self.sz)
        c = QColor()
        c.setHslF(h, s, 1)
        print(c)
        return c

class colorPickerWindow(QWidget):
    def __init__(self):
        super(colorPickerWindow, self).__init__()
        self.ly = QVBoxLayaout(self)
        self.color = QLabel()
        self.ly.addWidget(self.color)

if __name__ == '__main__':
    app = QApplication([])
    w = pickerClass()
    w.show()
    app.exec_()