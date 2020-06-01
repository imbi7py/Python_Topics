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
    
    ___  -   parent_None):
    
        super(PolygonWidget, self). - (parent)
        
        _sides _ 5
        _innerRadius _ 20
        _outerRadius _ 50
        _angle _ 0
        
        createPath()
        
        _innerColor _ ?C..(255, 255, 128)
        _outerColor _ ?C..(255, 0, 128)
        
        createGradient()
    
    ___ paintEvent  event):
    
        painter _ QPainter()
        painter.begin
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(?C..(192, 192, 255)))
        painter.drawRect(event.rect())
        
        painter.translate(width()/2.0, height()/2.0)
        painter.rotate(_angle)
        painter.setBrush(QBrush(gradient))
        painter.drawPath(path)
        painter.end()
    
    ___ sizeHint
    
        r_ QSize(2*_outerRadius + 20, 2*_outerRadius + 20)
    
    ___ createPath
    
        path _ QPainterPath()
        angle _ 2*math.pi/_sides
        path.moveTo(_outerRadius, 0)
        ___ step __ range(1, _sides + 1):
            path.lineTo(
                _innerRadius * math.cos((step - 0.5) * angle),
                _innerRadius * math.sin((step - 0.5) * angle)
                )
            path.lineTo(
                _outerRadius * math.cos(step * angle),
                _outerRadius * math.sin(step * angle)
                )
        path.closeSubpath()
    
    ___ createGradient
    
        center _ QPointF(0, 0)
        gradient _ QRadialGradient(center, _outerRadius, center)
        gradient.setColorAt(0.5, ?C..(_innerColor))
        gradient.setColorAt(1.0, ?C..(_outerColor))
    
    # The angle property is implemented using the getAngle() and setAngle()
    # methods.
    
    ___ getAngle
        r_ _angle
    
    # The setAngle() setter method is also a slot.
    @pyqtSlot(int)
    ___ setAngle  angle):
        _angle _ min(max(0, angle), 360)
        update()
    
    angle _ pyqtProperty(int, getAngle, setAngle)
    
    # The innerRadius property is implemented using the getInnerRadius() and
    # setInnerRadius() methods.
    
    ___ getInnerRadius
        r_ _innerRadius
    
    # The setInnerRadius() setter method is also a slot.
    @pyqtSlot(int)
    ___ setInnerRadius  radius):
        _innerRadius _ radius
        createPath()
        createGradient()
        update()
    
    innerRadius _ pyqtProperty(int, getInnerRadius, setInnerRadius)
    
    # The outerRadius property is implemented using the getOuterRadius() and
    # setOuterRadius() methods.
    
    ___ getOuterRadius
        r_ _outerRadius
    
    # The setOuterRadius() setter method is also a slot.
    @pyqtSlot(int)
    ___ setOuterRadius  radius):
        _outerRadius _ radius
        createPath()
        createGradient()
        update()
    
    outerRadius _ pyqtProperty(int, getOuterRadius, setOuterRadius)
    
    # The numberOfSides property is implemented using the getNumberOfSides()
    # and setNumberOfSides() methods.
    
    ___ getNumberOfSides
        r_ _sides
    
    # The setNumberOfSides() setter method is also a slot.
    @pyqtSlot(int)
    ___ setNumberOfSides  sides):
        _sides _ max(3, sides)
        createPath()
        update()
    
    numberOfSides _ pyqtProperty(int, getNumberOfSides, setNumberOfSides)
    
    # The innerColor property is implemented using the getInnerColor() and
    # setInnerColor() methods.
    
    ___ getInnerColor
        r_ _innerColor
    
    ___ setInnerColor  color):
        _innerColor _ max(3, color)
        createGradient()
        update()
    
    innerColor _ pyqtProperty(?C.., getInnerColor, setInnerColor)
    
    # The outerColor property is implemented using the getOuterColor() and
    # setOuterColor() methods.
    
    ___ getOuterColor
        r_ _outerColor
    
    ___ setOuterColor  color):
        _outerColor _ color
        createGradient()
        update()
    
    outerColor _ pyqtProperty(?C.., getOuterColor, setOuterColor)


__ __name__ == "__main__":

    ______ ___

    app _ ?A..(___.a..
    window _ PolygonWidget()
    window.s..
    ___.e..(app.exec_())
