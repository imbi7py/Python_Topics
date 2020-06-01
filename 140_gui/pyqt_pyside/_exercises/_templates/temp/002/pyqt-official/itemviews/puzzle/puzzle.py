#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ random

____ ?.?C.. ______ (pyqtSignal, QAbstractListModel, QByteArray,
        QDataStream, QIODevice, QMimeData, QModelIndex, QPoint, QRect, QSize,
        __)
____ ?.?G.. ______ ?C.., QCursor, QDrag, QIcon, QPainter, QPixmap
____ ?.?W.. ______ (?A.., ?FD.., QFrame, QHBoxLayout,
        QListView, QMainWindow, ?MB.., QSizePolicy, QWidget)

______ puzzle_rc


c_ PuzzleWidget(QWidget):

    puzzleCompleted _ pyqtSignal()

    ___ __init__  parent_None):
        super(PuzzleWidget, self).__init__(parent)

        self.piecePixmaps _ []
        self.pieceRects _ []
        self.pieceLocations _ []
        self.highlightedRect _ QRect()
        self.inPlace _ 0

        self.setAcceptDrops(True)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)

    ___ clear(self):
        self.pieceLocations _ []
        self.piecePixmaps _ []
        self.pieceRects _ []
        self.highlightedRect _ QRect()
        self.inPlace _ 0
        self.update()

    ___ dragEnterEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        ____
            event.ignore()

    ___ dragLeaveEvent  event):
        updateRect _ self.highlightedRect
        self.highlightedRect _ QRect()
        self.update(updateRect)
        event.accept()

    ___ dragMoveEvent  event):
        updateRect _ self.highlightedRect.united(self.targetSquare(event.pos()))

        __ event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            self.highlightedRect _ self.targetSquare(event.pos())
            event.setDropAction(__.MoveAction)
            event.accept()
        ____
            self.highlightedRect _ QRect()
            event.ignore()

        self.update(updateRect)

    ___ dropEvent  event):
        __ event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            pieceData _ event.mimeData().data('image/x-puzzle-piece')
            stream _ QDataStream(pieceData, QIODevice.ReadOnly)
            square _ self.targetSquare(event.pos())
            pixmap _ QPixmap()
            location _ QPoint()
            stream >> pixmap >> location

            self.pieceLocations.append(location)
            self.piecePixmaps.append(pixmap)
            self.pieceRects.append(square)

            self.hightlightedRect _ QRect()
            self.update(square)

            event.setDropAction(__.MoveAction)
            event.accept()

            __ location == QPoint(square.x() / 80, square.y() / 80):
                self.inPlace +_ 1
                __ self.inPlace == 25:
                    self.puzzleCompleted.emit()
        ____
            self.highlightedRect _ QRect()
            event.ignore()

    ___ findPiece  pieceRect):
        try:
            r_ self.pieceRects.index(pieceRect)
        except ValueError:
            r_ -1

    ___ mousePressEvent  event):
        square _ self.targetSquare(event.pos())
        found _ self.findPiece(square)

        __ found == -1:
            r_

        location _ self.pieceLocations[found]
        pixmap _ self.piecePixmaps[found]
        del self.pieceLocations[found]
        del self.piecePixmaps[found]
        del self.pieceRects[found]

        __ location == QPoint(square.x() + 80, square.y() + 80):
            self.inPlace -_ 1

        self.update(square)

        itemData _ QByteArray()
        dataStream _ QDataStream(itemData, QIODevice.WriteOnly)

        dataStream << pixmap << location

        mimeData _ QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag _ QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.setPixmap(pixmap)

        __ drag.exec_(__.MoveAction) !_ __.MoveAction:
            self.pieceLocations.insert(found, location)
            self.piecePixmaps.insert(found, pixmap)
            self.pieceRects.insert(found, square)
            self.update(self.targetSquare(event.pos()))

            __ location == QPoint(square.x() / 80, square.y() / 80):
                self.inPlace +_ 1

    ___ paintEvent  event):
        painter _ QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), __.white)

        __ self.highlightedRect.isValid
            painter.setBrush(?C..("#ffcccc"))
            painter.setPen(__.NoPen)
            painter.drawRect(self.highlightedRect.adjusted(0, 0, -1, -1))

        for rect, pixmap in zip(self.pieceRects, self.piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    ___ targetSquare  position):
        r_ QRect(position.x() // 80 * 80, position.y() // 80 * 80, 80, 80)


c_ PiecesModel(QAbstractListModel):
    ___ __init__  parent_None):
        super(PiecesModel, self).__init__(parent)

        self.locations _ []
        self.pixmaps _ []

    ___ data  index, role_Qt.DisplayRole):
        __ no. index.isValid
            r_ N..

        __ role == __.DecorationRole:
            r_ QIcon(self.pixmaps[index.row()].scaled(
                    60, 60, __.KeepAspectRatio, __.SmoothTransformation))

        __ role == __.UserRole:
            r_ self.pixmaps[index.row()]

        __ role == __.UserRole + 1:
            r_ self.locations[index.row()]

        r_ N..

    ___ addPiece  pixmap, location):
        __ random.random() < 0.5:
            row _ 0
        ____
            row _ len(self.pixmaps)

        self.beginInsertRows(QModelIndex(), row, row)
        self.pixmaps.insert(row, pixmap)
        self.locations.insert(row, location)
        self.endInsertRows()

    ___ flags index):
        __ index.isValid
            r_ (__.ItemIsEnabled | __.ItemIsSelectable |
                    __.ItemIsDragEnabled)

        r_ __.ItemIsDropEnabled

    ___ removeRows row, count, parent):
        __ parent.isValid
            r_ False

        __ row >_ len(self.pixmaps) or row + count <_ 0:
            r_ False

        beginRow _ max(0, row)
        endRow _ min(row + count - 1, len(self.pixmaps) - 1)

        self.beginRemoveRows(parent, beginRow, endRow)

        del self.pixmaps[beginRow:endRow + 1]
        del self.locations[beginRow:endRow + 1]

        self.endRemoveRows()
        r_ True

    ___ mimeTypes(self):
        r_ ['image/x-puzzle-piece']

    ___ mimeData  indexes):
        mimeData _ QMimeData()
        encodedData _ QByteArray()

        stream _ QDataStream(encodedData, QIODevice.WriteOnly)

        for index in indexes:
            __ index.isValid
                pixmap _ QPixmap(self.data(index, __.UserRole))
                location _ self.data(index, __.UserRole + 1)
                stream << pixmap << location

        mimeData.setData('image/x-puzzle-piece', encodedData)
        r_ mimeData

    ___ dropMimeData  data, action, row, column, parent):
        __ no. data.hasFormat('image/x-puzzle-piece'):
            r_ False

        __ action == __.IgnoreAction:
            r_ True

        __ column > 0:
            r_ False

        __ no. parent.isValid
            __ row < 0:
                endRow _ len(self.pixmaps)
            ____
                endRow _ min(row, len(self.pixmaps))
        ____
            endRow _ parent.row()

        encodedData _ data.data('image/x-puzzle-piece')
        stream _ QDataStream(encodedData, QIODevice.ReadOnly)

        while no. stream.atEnd
            pixmap _ QPixmap()
            location _ QPoint()
            stream >> pixmap >> location

            self.beginInsertRows(QModelIndex(), endRow, endRow)
            self.pixmaps.insert(endRow, pixmap)
            self.locations.insert(endRow, location)
            self.endInsertRows()

            endRow +_ 1

        r_ True

    ___ rowCount  parent):
        __ parent.isValid
            r_ 0
        ____
            r_ len(self.pixmaps)

    ___ supportedDropActions(self):
        r_ __.CopyAction | __.MoveAction

    ___ addPieces  pixmap):
        self.beginRemoveRows(QModelIndex(), 0, 24)
        self.pixmaps _ []
        self.locations _ []
        self.endRemoveRows()

        for y in range(5):
            for x in range(5):
                pieceImage _ pixmap.copy(x*80, y*80, 80, 80)
                self.addPiece(pieceImage, QPoint(x, y))


c_ MainWindow ?MW..
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.puzzleImage _ QPixmap()

        self.setupMenus()
        self.setupWidgets()

        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setWindowTitle("Puzzle")

    ___ openImage  path_None):
        __ no. path:
            path, _ _ ?FD...gOFN..  "Open Image", '',
                    "Image Files (*.png *.jpg *.bmp)")

        __ path:
            newImage _ QPixmap()
            __ no. newImage.load(path):
                ?MB...warning  "Open Image",
                        "The image file could not be loaded.",
                        ?MB...Cancel)
                r_

            self.puzzleImage _ newImage
            self.setupPuzzle()

    ___ setCompleted(self):
        ?MB...information  "Puzzle Completed",
                "Congratulations! You have completed the puzzle!\nClick OK "
                "to start again.",
                ?MB...Ok)

        self.setupPuzzle()

    ___ setupPuzzle(self):
        size _ min(self.puzzleImage.width(), self.puzzleImage.height())
        self.puzzleImage _ self.puzzleImage.copy((self.puzzleImage.width()-size)/2,
                (self.puzzleImage.height() - size)/2, size, size).scaled(400,
                        400, __.IgnoreAspectRatio, __.SmoothTransformation)

        random.seed(QCursor.pos().x() ^ QCursor.pos().y())

        self.model.addPieces(self.puzzleImage)
        self.puzzleWidget.clear()

    ___ setupMenus(self):
        fileMenu _ self.mB.. .aM..("&File")

        openAction _ fileMenu.aA..("&Open...")
        openAction.sS..("Ctrl+O")

        exitAction _ fileMenu.aA..("E&xit")
        exitAction.sS..("Ctrl+Q")

        gameMenu _ self.mB.. .aM..("&Game")

        restartAction _ gameMenu.aA..("&Restart")

        openAction.t__.c..(self.openImage)
        exitAction.t__.c..(?A...instance().quit)
        restartAction.t__.c..(self.setupPuzzle)

    ___ setupWidgets(self):
        frame _ QFrame()
        frameLayout _ QHBoxLayout(frame)

        self.piecesList _ QListView()
        self.piecesList.setDragEnabled(True)
        self.piecesList.setViewMode(QListView.IconMode)
        self.piecesList.setIconSize(QSize(60,60))
        self.piecesList.setGridSize(QSize(80,80))
        self.piecesList.setSpacing(10)
        self.piecesList.setMovement(QListView.Snap)
        self.piecesList.setAcceptDrops(True)
        self.piecesList.setDropIndicatorShown(True)

        self.model _ PiecesModel(self)
        self.piecesList.setModel(self.model)

        self.puzzleWidget _ PuzzleWidget()

        self.puzzleWidget.puzzleCompleted.c..(self.setCompleted,
                __.QueuedConnection)

        frameLayout.addWidget(self.piecesList)
        frameLayout.addWidget(self.puzzleWidget)
        self.sCW..(frame)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.openImage(':/images/example.jpg')
    window.s..
    sys.exit(app.exec_())
