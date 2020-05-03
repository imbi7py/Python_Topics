_____ ___
____ ?.?W.. _____ QMainWindow, ?A..
____ ?.?G.. _____ QPainter

____ demoToolBars _____ *

c_ AppWindow(QMainWindow
    ___  -
        s__. - ()
        ui _ Ui_MainWindow()
        ?.setupUi
        pos1 _ [0,0]
        pos2 _ [0,0]
        toDraw_""
        ?.actionCircle.triggered.c..(drawCircle)
        ?.actionRectangle.triggered.c..(drawRectangle)
        ?.actionLine.triggered.c..(drawLine)
        s..

    ___ paintEvent , event
        qp _ QPainter()
        qp.begin
        __ toDraw__"rectangle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]
            qp.drawRect(pos1[0], pos1[1], width, height)
        __ toDraw__"line":
            qp.drawLine(pos1[0], pos1[1], pos2[0], pos2[1])
        __ toDraw__"circle":
            width _ pos2[0]-pos1[0]
            height _ pos2[1] - pos1[1]
            rect _ ?C...QRect(pos1[0], pos1[1], width, height)
            startAngle _ 0
            arcLength _ 360 *16
            qp.drawArc(rect, startAngle, arcLength)      
        qp.end()
        
    ___ mousePressEvent , event
        __ event.buttons() & ?C...Qt.LeftButton:
            pos1[0], pos1[1] _ event.pos().x(), event.pos().y()
                        
    ___ mouseReleaseEvent , event
        pos2[0], pos2[1] _ event.pos().x(), event.pos().y()
        update()
               
    ___ drawCircle
        toDraw_"circle"

    ___ drawRectangle
        toDraw_"rectangle"

    ___ drawLine
        toDraw_"line"

app _ ?A..
w _ AppWindow()
w.s..
___.e.. ?.e




