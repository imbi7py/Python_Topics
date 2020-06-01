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


____ ?.?C.. ______ pyqtSignal, QMimeData, __
____ ?.?G.. ______ ?P.., QPixmap
____ ?.?W.. ______ (QAbstractItemView, ?A.., QDialogButtonBox,
        QFrame, QLabel, ?PB.., QTableWidget, QTableWidgetItem,
        QVBoxLayout, QWidget)


c_ DropArea(QLabel):

    changed _ pyqtSignal(QMimeData)

    ___ __init__  parent _ N..):
        super(DropArea, self).__init__(parent)

        self.setMinimumSize(200, 200)
        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setAlignment(__.AlignCenter)
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)
        self.clear()

    ___ dragEnterEvent  event):
        self.sT..("<drop content>")
        self.setBackgroundRole(?P...Highlight)
        event.acceptProposedAction()
        self.changed.emit(event.mimeData())

    ___ dragMoveEvent  event):
        event.acceptProposedAction()

    ___ dropEvent  event):
        mimeData _ event.mimeData()
        __ mimeData.hasImage
            self.setPixmap(QPixmap(mimeData.imageData()))
        ____ mimeData.hasHtml
            self.sT..(mimeData.html())
            self.setTextFormat(__.RichText)
        ____ mimeData.hasText
            self.sT..(mimeData.t__())
            self.setTextFormat(__.PlainText)
        ____ mimeData.hasUrls
            self.sT..("\n".join([url.path() for url in mimeData.urls()]))
        ____
            self.sT..("Cannot display data")

        self.setBackgroundRole(?P...Dark)
        event.acceptProposedAction()

    ___ dragLeaveEvent  event):
        self.clear()
        event.accept()

    ___ clear(self):
        self.sT..("<drop content>")
        self.setBackgroundRole(?P...Dark)
        self.changed.emit(N..)


c_ DropSiteWindow(QWidget):

    ___ __init__(self):
        super(DropSiteWindow, self).__init__()

        self.abstractLabel _ QLabel(
                "This example accepts drags from other applications and "
                "displays the MIME types provided by the drag object.")
        self.abstractLabel.setWordWrap(True)
        self.abstractLabel.adjustSize()

        self.dropArea _ DropArea()
        self.dropArea.changed.c..(self.updateFormatsTable)

        self.formatsTable _ QTableWidget()
        self.formatsTable.setColumnCount(2)
        self.formatsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formatsTable.setHorizontalHeaderLabels(["Format", "Content"])
        self.formatsTable.horizontalHeader().setStretchLastSection(True)

        self.clearButton _ ?PB..("Clear")
        self.quitButton _ ?PB..("Quit")

        self.buttonBox _ QDialogButtonBox()
        self.buttonBox.addButton(self.clearButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.quitButton.pressed.c..(self.close)
        self.clearButton.pressed.c..(self.dropArea.clear)

        mainLayout _ ?VBL..
        mainLayout.aW..(self.abstractLabel)
        mainLayout.aW..(self.dropArea)
        mainLayout.aW..(self.formatsTable)
        mainLayout.aW..(self.buttonBox)
        self.sL..(mainLayout)

        self.setWindowTitle("Drop Site")
        self.setMinimumSize(350, 500)

    ___ updateFormatsTable  mimeData_None):
        self.formatsTable.setRowCount(0)

        __ mimeData __ N..:
            r_

        for format in mimeData.formats
            formatItem _ QTableWidgetItem(format)
            formatItem.setFlags(__.ItemIsEnabled)
            formatItem.setTextAlignment(__.AlignTop | __.AlignLeft)

            __ format == 'text/plain':
                t__ _ mimeData.t__().strip()
            ____ format == 'text/html':
                t__ _ mimeData.html().strip()
            ____ format == 'text/uri-list':
                t__ _ " ".join([url.toString() for url in mimeData.urls()])
            ____
                t__ _ " ".join(["%02X" % ord(datum) for datum in mimeData.data(format)])

            row _ self.formatsTable.rowCount()
            self.formatsTable.insertRow(row)
            self.formatsTable.setItem(row, 0, QTableWidgetItem(format))
            self.formatsTable.setItem(row, 1, QTableWidgetItem(t__))

        self.formatsTable.resizeColumnToContents(0)


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ DropSiteWindow()
    window.s..
    ___.exit(app.exec_())

