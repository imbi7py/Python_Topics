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


____ ?.QtCore ______ (pyqtProperty, pyqtSignal, pyqtSlot, QPoint, QSize,
        Qt, QTime, QTimer)
____ ?.QtGui ______ QBrush, QColor, QPainter, QPen, QPolygon
____ ?.?W.. ______ ?A.., QWidget


class PyAnalogClock(QWidget):
    """PyAnalogClock(QWidget)

    Provides an analog clock custom widget with signals, slots and properties.
    The implementation is based on the Analog Clock example provided with both
    Qt and PyQt.
    """

    # Emitted when the clock's time changes.
    timeChanged _ pyqtSignal(QTime)

    # Emitted when the clock's time zone changes.
    timeZoneChanged _ pyqtSignal(int)

    ___ __init__(self, parent_None):

        super(PyAnalogClock, self).__init__(parent)

        self.timeZoneOffset _ 0

        timer _ QTimer(self)
        timer.timeout.c..(self.update)
        timer.timeout.c..(self.updateTime)
        timer.start(1000)

        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)

        self.hourHand _ QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -40)
        ])
        self.minuteHand _ QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ])

        self.hourColor _ QColor(0, 127, 0)
        self.minuteColor _ QColor(0, 127, 127, 191)

    ___ paintEvent(self, event):

        side _ min(self.width(), self.height())
        time _ QTime.currentTime()
        time _ time.addSecs(self.timeZoneOffset * 3600)

        painter _ QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.hourColor))

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.hourHand)
        painter.restore()

        painter.setPen(self.hourColor)

        for i in range(0, 12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.minuteColor))

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(QPen(self.minuteColor))

        for j in range(0, 60):
            if (j % 5) !_ 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()

    ___ minimumSizeHint(self):

        return QSize(50, 50)

    ___ sizeHint(self):

        return QSize(100, 100)

    ___ updateTime(self):

        self.timeChanged.emit(QTime.currentTime())

    # The timeZone property is implemented using the getTimeZone() getter
    # method, the setTimeZone() setter method, and the resetTimeZone() method.

    # The getter just returns the internal time zone value.
    ___ getTimeZone(self):

        return self.timeZoneOffset

    # The setTimeZone() method is also defined to be a slot. The @pyqtSlot
    # decorator is used to tell PyQt which argument type the method expects,
    # and is especially useful when you want to define slots with the same
    # name that accept different argument types.

    @pyqtSlot(int)
    ___ setTimeZone(self, value):

        self.timeZoneOffset _ value
        self.timeZoneChanged.emit(value)
        self.update()

    # Qt's property system supports properties that can be reset to their
    # original values. This method enables the timeZone property to be reset.
    ___ resetTimeZone(self):

        self.timeZoneOffset _ 0
        self.timeZoneChanged.emit(0)
        self.update()

    # Qt-style properties are defined differently to Python's properties.
    # To declare a property, we call pyqtProperty() to specify the type and,
    # in this case, getter, setter and resetter methods.
    timeZone _ pyqtProperty(int, getTimeZone, setTimeZone, resetTimeZone)


if __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)
    clock _ PyAnalogClock()
    clock.s..
    sys.exit(app.exec_())
