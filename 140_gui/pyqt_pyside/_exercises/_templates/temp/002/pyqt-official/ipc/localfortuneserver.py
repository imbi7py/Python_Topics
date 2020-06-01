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
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


______ random

____ ?.?C.. ______ QByteArray, QDataStream, QIODevice
____ ?.?W.. ______ (?A.., QDialog, QLabel, QHBoxLayout,
        ?MB.., ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QLocalServer


c_ Server(QDialog):
    ___ __init__  parent_None):
        super(Server, self).__init__(parent)

        statusLabel _ QLabel()
        statusLabel.setWordWrap(True)
        quitButton _ ?PB..("Quit")
        quitButton.setAutoDefault F..

        self.fortunes _ (
            "You've been leading a dog's life. Stay off the furniture.",
            "You've got to think about tomorrow.",
            "You will be surprised by a loud noise.",
            "You will feel hungry again in another hour.",
            "You might have mail.",
            "You cannot kill time without injuring eternity.",
            "Computers are not intelligent. They only think they are.",
        )

        self.server _ QLocalServer()
        __ no. self.server.listen('fortune'):
            ?MB...critical  "Fortune Server",
                    "Unable to start the server: %s." % self.server.errorString())
            self.close()
            r_

        statusLabel.sT..("The server is running.\nRun the Fortune Client "
                "example now.")

        quitButton.c__.c..(self.close)
        self.server.newConnection.c..(self.sendFortune)

        buttonLayout _ QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.aW..(quitButton)
        buttonLayout.addStretch(1)

        mainLayout _ ?VBL..
        mainLayout.aW..(statusLabel)
        mainLayout.addLayout(buttonLayout)
        self.sL..(mainLayout)

        self.setWindowTitle("Fortune Server")

    ___ sendFortune(self):
        block _ QByteArray()
        out _ QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        out.writeQString(random.choice(self.fortunes))
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)

        clientConnection _ self.server.nextPendingConnection()
        clientConnection.disconnected.c..(clientConnection.deleteLater)
        clientConnection.w..(block)
        clientConnection.flush()
        clientConnection.disconnectFromServer()


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    server _ Server()
    server.s..
    ___.exit(app.exec_())
