# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsPixmapItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

pix = QtGui.QPixmap("foto.jpg")
mask = QtGui.QBitmap(pix.size())
mask.clear()
painter = QtGui.QPainter()
painter.begin(mask)
painter.setPen(QtCore.Qt.color1)
painter.setBrush(QtCore.Qt.color1)
painter.setRenderHint(QtGui.QPainter.Antialiasing)
painter.drawEllipse(50, 50, 400, 250)
painter.end()
pix.setMask(mask)

item = QtGui.QGraphicsPixmapItem()
item.setPixmap(pix)
item.setOffset(50, 50)
item.setShapeMode(QtGui.QGraphicsPixmapItem.MaskShape)

item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
item.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
item.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
scene.addItem(item)

view = QtGui.QGraphicsView(scene)

box = QtGui.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec_())