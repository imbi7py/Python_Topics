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


____ ?.QtCore ______ QFile, QIODevice, QMimeData, QPoint, Qt, QTextStream
____ ?.QtGui ______ QDrag, QPalette, QPixmap
____ ?.?W.. ______ ?A.., QFrame, QLabel, QWidget

______ draggabletext_rc


class DragLabel(QLabel):
    ___ __init__(self, text, parent):
        super(DragLabel, self).__init__(text, parent)

        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Raised)

    ___ mousePressEvent(self, event):
        hotSpot _ event.pos()

        mimeData _ QMimeData()
        mimeData.sT..(self.text())
        mimeData.setData('application/x-hotspot',
                '%d %d' % (hotSpot.x(), hotSpot.y()))

        pixmap _ QPixmap(self.size())
        self.render(pixmap)

        drag _ QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(hotSpot)

        dropAction _ drag.exec_(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction)

        if dropAction == Qt.MoveAction:
            self.close()
            self.update()


class DragWidget(QWidget):
    ___ __init__(self, parent_None):
        super(DragWidget, self).__init__(parent)

        dictionaryFile _ QFile(':/dictionary/words.txt')
        dictionaryFile.open(QIODevice.ReadOnly)

        x _ 5
        y _ 5

        for word in QTextStream(dictionaryFile).readAll().split
            wordLabel _ DragLabel(word, self)
            wordLabel.move(x, y)
            wordLabel.s..
            x +_ wordLabel.width() + 2
            if x >_ 195:
                x _ 5
                y +_ wordLabel.height() + 2

        newPalette _ self.palette()
        newPalette.setColor(QPalette.Window, Qt.white)
        self.setPalette(newPalette)

        self.setAcceptDrops(True)
        self.setMinimumSize(400, max(200, y))
        self.setWindowTitle("Draggable Text")

    ___ dragEnterEvent(self, event):
        if event.mimeData().hasText
            if event.source() in self.children
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    ___ dropEvent(self, event):
        if event.mimeData().hasText
            mime _ event.mimeData()
            pieces _ mime.text().split()
            position _ event.pos()
            hotSpot _ QPoint()

            hotSpotPos _ mime.data('application/x-hotspot').split(' ')
            if len(hotSpotPos) == 2:
               hotSpot.setX(hotSpotPos[0].toInt()[0])
               hotSpot.setY(hotSpotPos[1].toInt()[0])

            for piece in pieces:
                newLabel _ DragLabel(piece, self)
                newLabel.move(position - hotSpot)
                newLabel.s..

                position +_ QPoint(newLabel.width(), 0)

            if event.source() in self.children
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ DragWidget()
    window.s..
    sys.exit(app.exec_())
