#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
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


____ ?.?C.. ______ (pyqtSignal, QBuffer, QByteArray, QFile, QIODevice,
        QMimeData, __)
____ ?.?G.. ______ QDrag, QIcon, QImage, QPainter, QPixmap
____ ?.?W.. ______ (?A.., QGridLayout, QLabel, ?PB..,
        QScrollArea, QWidget)
____ ?.QtSvg ______ QSvgWidget

______ delayedencoding_rc


c_ MimeData(QMimeData):

    dataRequested _ pyqtSignal(str)

    ___ formats(self):
        formats _ QMimeData.formats(self)
        formats.ap..('image/png')

        r_ formats

    ___ retrieveData  mimeType, qvtype):
        self.dataRequested.emit(mimeType)

        r_ QMimeData.retrieveData  mimeType, qvtype)


c_ SourceWidget(QWidget):
    ___ __init__  parent_None):
        super(SourceWidget, self).__init__(parent)

        self.mimeData _ N..

        imageFile _ QFile(':/images/example.svg')
        imageFile.o..(QIODevice.ReadOnly)
        self.imageData _ imageFile.readAll()
        imageFile.close()

        imageArea _ QScrollArea()
        self.imageLabel _ QSvgWidget()
        self.imageLabel.renderer().load(self.imageData)
        imageArea.setWidget(self.imageLabel)

        instructTopLabel _ QLabel("This is an SVG drawing:")
        instructBottomLabel _ QLabel("Drag the icon to copy the drawing as a PNG file:")
        dragIcon _ ?PB..("Export")
        dragIcon.setIcon(QIcon(':/images/drag.png'))
        dragIcon.pressed.c..(self.startDrag)

        layout _ QGridLayout()
        layout.aW..(instructTopLabel, 0, 0, 1, 2)
        layout.aW..(imageArea, 1, 0, 2, 2)
        layout.aW..(instructBottomLabel, 3, 0)
        layout.aW..(dragIcon, 3, 1)
        self.sL..(layout)
        self.setWindowTitle("Delayed Encoding")

    ___ createData  mimeType):
        __ mimeType !_ 'image/png':
            r_

        image _ QImage(self.imageLabel.size(), QImage.Format_RGB32)
        painter _ QPainter()
        painter.begin(image)
        self.imageLabel.renderer().render(painter)
        painter.end()

        data _ QByteArray()
        buffer _ QBuffer(data)
        buffer.o..(QIODevice.WriteOnly)
        image.save(buffer, 'PNG')
        buffer.close()
        self.mimeData.setData('image/png', data)

    ___ startDrag(self):
        self.mimeData _ MimeData()
        self.mimeData.dataRequested.c..(self.createData, __.DirectConnection)

        drag _ QDrag(self)
        drag.setMimeData(self.mimeData)
        drag.setPixmap(QPixmap(':/images/drag.png'))
        drag.exec_(__.CopyAction)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    window _ SourceWidget()
    window.s..
    sys.exit(app.exec_())
