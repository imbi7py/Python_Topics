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


____ math ______ cos, pi, sin

____ ?.?C.. ______ QSize, __
____ ?.?G.. ______ (QBrush, ?C.., QFont, QLinearGradient, QPainter,
        QPainterPath, ?P.., QPen)
____ ?.?W.. ______ (?A.., QComboBox, QGridLayout, QLabel,
        QSizePolicy, QSpinBox, QWidget)


c_ RenderArea(QWidget):
    ___ __init__  path, parent_None):
        super(RenderArea, self).__init__(parent)

        self.path _ path

        self.penWidth _ 1
        self.rotationAngle _ 0
        self.setBackgroundRole(?P...Base)

    ___ minimumSizeHint(self):
        r_ QSize(50, 50)

    ___ sizeHint(self):
        r_ QSize(100, 100)

    ___ setFillRule  rule):
        self.path.setFillRule(rule)
        self.update()

    ___ setFillGradient  color1, color2):
        self.fillColor1 _ color1
        self.fillColor2 _ color2
        self.update()

    ___ setPenWidth  width):
        self.penWidth _ width
        self.update()

    ___ setPenColor  color):
        self.penColor _ color
        self.update()

    ___ setRotationAngle  degrees):
        self.rotationAngle _ degrees
        self.update()

    ___ paintEvent  event):
        painter _ QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(self.width() / 100.0, self.height() / 100.0)
        painter.translate(50.0, 50.0)
        painter.rotate(-self.rotationAngle)
        painter.translate(-50.0, -50.0)

        painter.setPen(
                QPen(self.penColor, self.penWidth, __.SolidLine, __.RoundCap,
                        __.RoundJoin))
        gradient _ QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.0, self.fillColor1)
        gradient.setColorAt(1.0, self.fillColor2)
        painter.setBrush(QBrush(gradient))
        painter.drawPath(self.path)


c_ Window(QWidget):
    NumRenderAreas _ 9

    ___ __init__(self):
        super(Window, self).__init__()

        rectPath _ QPainterPath()
        rectPath.moveTo(20.0, 30.0)
        rectPath.lineTo(80.0, 30.0)
        rectPath.lineTo(80.0, 70.0)
        rectPath.lineTo(20.0, 70.0)
        rectPath.closeSubpath()

        roundRectPath _ QPainterPath()
        roundRectPath.moveTo(80.0, 35.0)
        roundRectPath.arcTo(70.0, 30.0, 10.0, 10.0, 0.0, 90.0)
        roundRectPath.lineTo(25.0, 30.0)
        roundRectPath.arcTo(20.0, 30.0, 10.0, 10.0, 90.0, 90.0)
        roundRectPath.lineTo(20.0, 65.0)
        roundRectPath.arcTo(20.0, 60.0, 10.0, 10.0, 180.0, 90.0)
        roundRectPath.lineTo(75.0, 70.0)
        roundRectPath.arcTo(70.0, 60.0, 10.0, 10.0, 270.0, 90.0)
        roundRectPath.closeSubpath()

        ellipsePath _ QPainterPath()
        ellipsePath.moveTo(80.0, 50.0)
        ellipsePath.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)

        piePath _ QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.lineTo(65.0, 32.6795)
        piePath.arcTo(20.0, 30.0, 60.0, 40.0, 60.0, 240.0)
        piePath.closeSubpath()

        polygonPath _ QPainterPath()
        polygonPath.moveTo(10.0, 80.0)
        polygonPath.lineTo(20.0, 10.0)
        polygonPath.lineTo(80.0, 30.0)
        polygonPath.lineTo(90.0, 70.0)
        polygonPath.closeSubpath()

        groupPath _ QPainterPath()
        groupPath.moveTo(60.0, 40.0)
        groupPath.arcTo(20.0, 20.0, 40.0, 40.0, 0.0, 360.0)
        groupPath.moveTo(40.0, 40.0)
        groupPath.lineTo(40.0, 80.0)
        groupPath.lineTo(80.0, 80.0)
        groupPath.lineTo(80.0, 40.0)
        groupPath.closeSubpath()

        textPath _ QPainterPath()
        timesFont _ QFont('Times', 50)
        timesFont.setStyleStrategy(QFont.ForceOutline)
        textPath.addText(10, 70, timesFont, "Qt")

        bezierPath _ QPainterPath()
        bezierPath.moveTo(20, 30)
        bezierPath.cubicTo(80, 0, 50, 50, 80, 80)

        starPath _ QPainterPath()
        starPath.moveTo(90, 50)
        for i in range(1, 5):
            starPath.lineTo(50 + 40 * cos(0.8 * i * pi),
                    50 + 40 * sin(0.8 * i * pi))
        starPath.closeSubpath()

        self.renderAreas _ [RenderArea(rectPath), RenderArea(roundRectPath),
                RenderArea(ellipsePath), RenderArea(piePath),
                RenderArea(polygonPath), RenderArea(groupPath),
                RenderArea(textPath), RenderArea(bezierPath),
                RenderArea(starPath)]
        assert le.(self.renderAreas) == 9

        self.fillRuleComboBox _ QComboBox()
        self.fillRuleComboBox.addItem("Odd Even", __.OddEvenFill)
        self.fillRuleComboBox.addItem("Winding", __.WindingFill)

        fillRuleLabel _ QLabel("Fill &Rule:")
        fillRuleLabel.setBuddy(self.fillRuleComboBox)

        self.fillColor1ComboBox _ QComboBox()
        self.populateWithColors(self.fillColor1ComboBox)
        self.fillColor1ComboBox.setCurrentIndex(
                self.fillColor1ComboBox.findText("mediumslateblue"))

        self.fillColor2ComboBox _ QComboBox()
        self.populateWithColors(self.fillColor2ComboBox)
        self.fillColor2ComboBox.setCurrentIndex(
                self.fillColor2ComboBox.findText("cornsilk"))

        fillGradientLabel _ QLabel("&Fill Gradient:")
        fillGradientLabel.setBuddy(self.fillColor1ComboBox)

        fillToLabel _ QLabel("to")
        fillToLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.penWidthSpinBox _ QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)

        penWidthLabel _ QLabel("&Pen Width:")
        penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penColorComboBox _ QComboBox()
        self.populateWithColors(self.penColorComboBox)
        self.penColorComboBox.setCurrentIndex(
                self.penColorComboBox.findText('darkslateblue'))

        penColorLabel _ QLabel("Pen &Color:")
        penColorLabel.setBuddy(self.penColorComboBox)

        self.rotationAngleSpinBox _ QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix(u'\N{DEGREE SIGN}')

        rotationAngleLabel _ QLabel("&Rotation Angle:")
        rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)

        self.fillRuleComboBox.activated.c..(self.fillRuleChanged)
        self.fillColor1ComboBox.activated.c..(self.fillGradientChanged)
        self.fillColor2ComboBox.activated.c..(self.fillGradientChanged)
        self.penColorComboBox.activated.c..(self.penColorChanged)

        for i in range(Window.NumRenderAreas):
            self.penWidthSpinBox.valueChanged.c..(self.renderAreas[i].setPenWidth)
            self.rotationAngleSpinBox.valueChanged.c..(self.renderAreas[i].setRotationAngle)

        topLayout _ QGridLayout()
        for i in range(Window.NumRenderAreas):
            topLayout.aW..(self.renderAreas[i], i / 3, i % 3)

        mainLayout _ QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 4)
        mainLayout.aW..(fillRuleLabel, 1, 0)
        mainLayout.aW..(self.fillRuleComboBox, 1, 1, 1, 3)
        mainLayout.aW..(fillGradientLabel, 2, 0)
        mainLayout.aW..(self.fillColor1ComboBox, 2, 1)
        mainLayout.aW..(fillToLabel, 2, 2)
        mainLayout.aW..(self.fillColor2ComboBox, 2, 3)
        mainLayout.aW..(penWidthLabel, 3, 0)
        mainLayout.aW..(self.penWidthSpinBox, 3, 1, 1, 3)
        mainLayout.aW..(penColorLabel, 4, 0)
        mainLayout.aW..(self.penColorComboBox, 4, 1, 1, 3)
        mainLayout.aW..(rotationAngleLabel, 5, 0)
        mainLayout.aW..(self.rotationAngleSpinBox, 5, 1, 1, 3)
        self.sL..(mainLayout)

        self.fillRuleChanged()
        self.fillGradientChanged()
        self.penColorChanged()
        self.penWidthSpinBox.setValue(2)

        self.setWindowTitle("Painter Paths")

    ___ fillRuleChanged(self):
        rule _ __.FillRule(self.currentItemData(self.fillRuleComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillRule(rule)

    ___ fillGradientChanged(self):
        color1 _ ?C..(self.currentItemData(self.fillColor1ComboBox))
        color2 _ ?C..(self.currentItemData(self.fillColor2ComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillGradient(color1, color2)

    ___ penColorChanged(self):
        color _ ?C..(self.currentItemData(self.penColorComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setPenColor(color)

    ___ populateWithColors  comboBox):
        colorNames _ ?C...colorNames()
        for name in colorNames:
            comboBox.addItem(name, name)

    ___ currentItemData  comboBox):
        r_ comboBox.itemData(comboBox.currentIndex())


__ __name__ == '__main__':

    ______ ___

    app _ ?A..(___.argv)
    window _ Window()
    window.s..
    ___.exit(app.exec_())
