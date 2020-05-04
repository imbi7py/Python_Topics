____ ?.?C.. _____ _
____ ?.?G.. _____ _

c_ splineRampWidget(?W..
    ___  -
        s__(splineRampWidget, self). -
        resize(300, 200)

        lineWidth _ 3
        pointSize _ 10

        point1 _ QPointF(0, 0)
        point2 _ QPointF(300, 200)

        factor1 _ 0.0
        factor2 _ 1.0

        dragged _ N..

        region1 _ ?R..
        region2 _ ?R..
        regionSize _ 40
        updateRegions

    ___ updateRegions
        region1 _ ?R..(0, 0, regionSize, regionSize)
        region1.moveCenter(point1.toPoint())

        region2 _ ?R..(0, 0, regionSize, regionSize)
        region2.moveCenter(point2.toPoint())

        factor1 _ point1.y / fl..(size.height())
        factor2 _ point2.y / fl..(size.height())
        print factor1, factor2

    ___ paintEvent , event
        rec _ event.rect
        painter _ ?P..
        painter.b..
        painter.setRenderHint(?P...Antialiasing)
        painter.fillRect(event.rect, __.b..)
        path _ QPainterPath
        path.moveTo(point1)
        path.cubicTo(rec.width/2, point1.y,
                     rec.width/2, point2.y,
                     rec.width, point2.y())
        painter.sP..(?P..(QBrush(__.white), lineWidth))
        painter.drawPath(path)
        painter.setBrush(QBrush(__.white))

        painter.drawEllipse(point1, pointSize, pointSize)
        painter.drawEllipse(point2, pointSize, pointSize)

        painter.sP..(?P..(QBrush(__.white), 1))
        painter.setBrush(__.NoBrush)
        painter.dR..(region1)
        painter.dR..(region2)
        painter.e..

    ___ mPE.. , event
        # print self.region1.contains(event.pos())
        __ region1.contains(event.p..()):
            dragged _ point1
        ____ region2.contains(event.p..()):
            dragged _ point2
        s__(splineRampWidget, self).mPE..(event)

    ___ mouseMoveEvent , event
        # print self.dragged
        __ no. dragged __ N..:
            y _ event.p...y
            s _ size
            dragged.setY(min(max(y, 1), s.height()))
            update
        s__(splineRampWidget, self).mouseMoveEvent(event)

    ___ mouseReleaseEvent , event
        dragged _ N..
        updateRegions
        update
        s__(splineRampWidget, self).mRE..(event)

    ___ resizeEvent , event

        point1.setY(event.size.height * factor1)
        point2.setY(event.size.height * factor2)
        point2.setX(event.size.width())
        updateRegions
        update
        s__(splineRampWidget, self).resizeEvent(event)

__ _____ __ ______
    app _ ?A..
    w _ splineRampWidget
    w.s..
    app.e..