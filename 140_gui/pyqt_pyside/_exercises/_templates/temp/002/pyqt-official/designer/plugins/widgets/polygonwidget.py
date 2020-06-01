#!/usr/bin/env python

"""
polygonwidget.py

A PyQt custom widget example for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

______ math

____ ?.?C.. ______ pyqtProperty, pyqtSlot, QPointF, QSize
____ ?.?G.. ______ QBrush, ?C.., QPainter, QPainterPath, QRadialGradient
____ ?.?W.. ______ ?A.., QWidget


c_ PolygonWidget(QWidget):
    """PolygonWidget(QWidget)
    
    Provides a custom widget to display a polygon with properties and slots
    that can be used to customize its appearance.
    """
    
    ___ __init__  parent_None):
    
        super(PolygonWidget, self).__init__(parent)
        
        self._sides _ 5
        self._innerRadius _ 20
        self._outerRadius _ 50
        self._angle _ 0
        
        self.createPath()
        
        self._innerColor _ ?C..(255, 255, 128)
        self._outerColor _ ?C..(255, 0, 128)
        
        self.createGradient()
    
    ___ paintEvent  event):
    
        painter _ QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(?C..(192, 192, 255)))
        painter.drawRect(event.rect())
        
        painter.translate(self.width()/2.0, self.height()/2.0)
        painter.rotate(self._angle)
        painter.setBrush(QBrush(self.gradient))
        painter.drawPath(self.path)
        painter.end()
    
    ___ sizeHint(self):
    
        r_ QSize(2*self._outerRadius + 20, 2*self._outerRadius + 20)
    
    ___ createPath(self):
    
        self.path _ QPainterPath()
        angle _ 2*math.pi/self._sides
        self.path.moveTo(self._outerRadius, 0)
        for step in range(1, self._sides + 1):
            self.path.lineTo(
                self._innerRadius * math.cos((step - 0.5) * angle),
                self._innerRadius * math.sin((step - 0.5) * angle)
                )
            self.path.lineTo(
                self._outerRadius * math.cos(step * angle),
                self._outerRadius * math.sin(step * angle)
                )
        self.path.closeSubpath()
    
    ___ createGradient(self):
    
        center _ QPointF(0, 0)
        self.gradient _ QRadialGradient(center, self._outerRadius, center)
        self.gradient.setColorAt(0.5, ?C..(self._innerColor))
        self.gradient.setColorAt(1.0, ?C..(self._outerColor))
    
    # The angle property is implemented using the getAngle() and setAngle()
    # methods.
    
    ___ getAngle(self):
        r_ self._angle
    
    # The setAngle() setter method is also a slot.
    @pyqtSlot(int)
    ___ setAngle  angle):
        self._angle _ min(max(0, angle), 360)
        self.update()
    
    angle _ pyqtProperty(int, getAngle, setAngle)
    
    # The innerRadius property is implemented using the getInnerRadius() and
    # setInnerRadius() methods.
    
    ___ getInnerRadius(self):
        r_ self._innerRadius
    
    # The setInnerRadius() setter method is also a slot.
    @pyqtSlot(int)
    ___ setInnerRadius  radius):
        self._innerRadius _ radius
        self.createPath()
        self.createGradient()
        self.update()
    
    innerRadius _ pyqtProperty(int, getInnerRadius, setInnerRadius)
    
    # The outerRadius property is implemented using the getOuterRadius() and
    # setOuterRadius() methods.
    
    ___ getOuterRadius(self):
        r_ self._outerRadius
    
    # The setOuterRadius() setter method is also a slot.
    @pyqtSlot(int)
    ___ setOuterRadius  radius):
        self._outerRadius _ radius
        self.createPath()
        self.createGradient()
        self.update()
    
    outerRadius _ pyqtProperty(int, getOuterRadius, setOuterRadius)
    
    # The numberOfSides property is implemented using the getNumberOfSides()
    # and setNumberOfSides() methods.
    
    ___ getNumberOfSides(self):
        r_ self._sides
    
    # The setNumberOfSides() setter method is also a slot.
    @pyqtSlot(int)
    ___ setNumberOfSides  sides):
        self._sides _ max(3, sides)
        self.createPath()
        self.update()
    
    numberOfSides _ pyqtProperty(int, getNumberOfSides, setNumberOfSides)
    
    # The innerColor property is implemented using the getInnerColor() and
    # setInnerColor() methods.
    
    ___ getInnerColor(self):
        r_ self._innerColor
    
    ___ setInnerColor  color):
        self._innerColor _ max(3, color)
        self.createGradient()
        self.update()
    
    innerColor _ pyqtProperty(?C.., getInnerColor, setInnerColor)
    
    # The outerColor property is implemented using the getOuterColor() and
    # setOuterColor() methods.
    
    ___ getOuterColor(self):
        r_ self._outerColor
    
    ___ setOuterColor  color):
        self._outerColor _ color
        self.createGradient()
        self.update()
    
    outerColor _ pyqtProperty(?C.., getOuterColor, setOuterColor)


__ __name__ == "__main__":

    ______ ___

    app _ ?A..(___.argv)
    window _ PolygonWidget()
    window.s..
    ___.exit(app.exec_())
