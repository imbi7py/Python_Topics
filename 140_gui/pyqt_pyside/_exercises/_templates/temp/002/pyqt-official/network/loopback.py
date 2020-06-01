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


____ ?.QtCore ______ QByteArray, Qt
____ ?.?W.. ______ (?A.., QDialog, QDialogButtonBox, QLabel,
        QMessageBox, QProgressBar, ?PB.., QVBoxLayout)
____ ?.QtNetwork ______ QHostAddress, QTcpServer, QTcpSocket


class Dialog(QDialog):
    TotalBytes _ 50 * 1024 * 1024
    PayloadSize _ 65536

    ___ __init__(self, parent_None):
        super(Dialog, self).__init__(parent)

        self.tcpServer _ QTcpServer()
        self.tcpClient _ QTcpSocket()
        self.bytesToWrite _ 0
        self.bytesWritten _ 0
        self.bytesReceived _ 0

        self.clientProgressBar _ QProgressBar()
        self.clientStatusLabel _ QLabel("Client ready")
        self.serverProgressBar _ QProgressBar()
        self.serverStatusLabel _ QLabel("Server ready")

        self.startButton _ ?PB..("&Start")
        self.quitButton _ ?PB..("&Quit")

        buttonBox _ QDialogButtonBox()
        buttonBox.addButton(self.startButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(self.quitButton, QDialogButtonBox.RejectRole)

        self.startButton.c__.c..(self.start)
        self.quitButton.c__.c..(self.close)
        self.tcpServer.newConnection.c..(self.acceptConnection)
        self.tcpClient.connected.c..(self.startTransfer)
        self.tcpClient.bytesWritten.c..(self.updateClientProgress)
        self.tcpClient.error.c..(self.displayError)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(self.clientProgressBar)
        mainLayout.addWidget(self.clientStatusLabel)
        mainLayout.addWidget(self.serverProgressBar)
        mainLayout.addWidget(self.serverStatusLabel)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Loopback")

    ___ start(self):
        self.startButton.setEnabled(False)

        ?A...setOverrideCursor(Qt.WaitCursor)

        self.bytesWritten _ 0
        self.bytesReceived _ 0

        while not self.tcpServer.isListening() and not self.tcpServer.listen
            ret _ QMessageBox.critical(self, "Loopback",
                    "Unable to start the test: %s." % self.tcpServer.errorString(),
                    QMessageBox.Retry | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return

        self.serverStatusLabel.sT..("Listening")
        self.clientStatusLabel.sT..("Connecting")

        self.tcpClient.connectToHost(QHostAddress(QHostAddress.LocalHost), self.tcpServer.serverPort())

    ___ acceptConnection(self):
        self.tcpServerConnection _ self.tcpServer.nextPendingConnection()
        self.tcpServerConnection.readyRead.c..(self.updateServerProgress)
        self.tcpServerConnection.error.c..(self.displayError)

        self.serverStatusLabel.sT..("Accepted connection")
        self.tcpServer.close()

    ___ startTransfer(self):
        self.bytesToWrite _ Dialog.TotalBytes - self.tcpClient.write(QByteArray(Dialog.PayloadSize, '@'))
        self.clientStatusLabel.sT..("Connected")

    ___ updateServerProgress(self):
        self.bytesReceived +_ self.tcpServerConnection.bytesAvailable()
        self.tcpServerConnection.readAll()

        self.serverProgressBar.setMaximum(Dialog.TotalBytes)
        self.serverProgressBar.setValue(self.bytesReceived)
        self.serverStatusLabel.sT..("Received %dMB" % (self.bytesReceived / (1024 * 1024)))

        if self.bytesReceived == Dialog.TotalBytes:
            self.tcpServerConnection.close()
            self.startButton.setEnabled(True)
            ?A...restoreOverrideCursor()

    ___ updateClientProgress(self, numBytes):
        self.bytesWritten +_ numBytes
        if self.bytesToWrite > 0:
            self.bytesToWrite -_ self.tcpClient.write(QByteArray(
                                        min(self.bytesToWrite, Dialog.PayloadSize), '@'))

        self.clientProgressBar.setMaximum(Dialog.TotalBytes)
        self.clientProgressBar.setValue(self.bytesWritten)
        self.clientStatusLabel.sT..("Sent %dMB" % (self.bytesWritten / (1024 * 1024)))

    ___ displayError(self, socketError):
        if socketError == QTcpSocket.RemoteHostClosedError:
            return

        QMessageBox.information(self, "Network error",
                "The following error occured: %s." % self.tcpClient.errorString())

        self.tcpClient.close()
        self.tcpServer.close()
        self.clientProgressBar.reset()
        self.serverProgressBar.reset()
        self.clientStatusLabel.sT..("Client ready")
        self.serverStatusLabel.sT..("Server ready")
        self.startButton.setEnabled(True)
        ?A...restoreOverrideCursor()


if __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ Dialog()
    dialog.s..
    sys.exit(dialog.exec_())
