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


______ math

____ ?.?C.. ______ (pS.., QBasicTimer, QObject, QPoint, QPointF,
        QRect, ?S.., QStandardPaths, __, QUrl)
____ ?.?G.. ______ (?C.., QDesktopServices, QImage, QPainter,
        QPainterPath, QPixmap, QRadialGradient)
____ ?.?W.. ______ ?A.., ?A.., QMainWindow, ?W..
____ ?.QtNetwork ______ (QNetworkAccessManager, QNetworkDiskCache,
        QNetworkRequest)


# how long (milliseconds) the user need to hold (after a tap on the screen)
# before triggering the magnifying glass feature
# 701, a prime number, is the sum of 229, 233, 239
# (all three are also prime numbers, consecutive!)
HOLD_TIME _ 701

# maximum size of the magnifier
# Hint: see above to find why I picked self one :)
MAX_MAGNIFIER _ 229

# tile size in pixels
TDIM _ 256


c_ Point(QPoint):
    """QPoint, that is fully qualified as a dict key"""
    ___  -   *par):
        __ par:
            super(Point, self). - (*par)
        ____
            super(Point, self). - ()

    ___ __hash__ 
        r_ x() * 17 ^ y()

    ___ __repr__ 
        r_ "Point(%s, %s)" % (x(), y())


___ tileForCoordinate(lat, lng, zoom):
    zn _ float(1 << zoom)
    tx _ float(lng + 180.0) / 360.0
    ty _ (1.0 - math.log(math.tan(lat * math.pi / 180.0) +
          1.0 / math.cos(lat * math.pi / 180.0)) / math.pi) / 2.0

    r_ QPointF(tx * zn, ty * zn)


___ longitudeFromTile(tx, zoom):
    zn _ float(1 << zoom)
    lat _ tx / zn * 360.0 - 180.0

    r_ lat


___ latitudeFromTile(ty, zoom):
    zn _ float(1 << zoom)
    n _ math.pi - 2 * math.pi * ty / zn
    lng _ 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))

    r_ lng


c_ SlippyMap(QObject):

    updated _ pS..(QRect)

    ___  -   parent_None):
        super(SlippyMap, self). - (parent)

        _offset _ QPoint()
        _tilesRect _ QRect()
        _tilePixmaps _   # dict # Point(x, y) to QPixmap mapping
        _manager _ QNetworkAccessManager()
        _url _ QUrl()
        # public vars
        width _ 400
        height _ 300
        zoom _ 15
        latitude _ 59.9138204
        longitude _ 10.7387413

        _emptyTile _ QPixmap(TDIM, TDIM)
        _emptyTile.fill(__.lightGray)

        cache _ QNetworkDiskCache()
        cache.setCacheDirectory(
            QStandardPaths.writableLocation(QStandardPaths.CacheLocation))
        _manager.setCache(cache)
        _manager.finished.c..(handleNetworkData)

    ___ invalidate 
        __ width <_ 0 or height <_ 0:
            r_

        ct _ tileForCoordinate(latitude, longitude, zoom)
        tx _ ct.x()
        ty _ ct.y()

        # top-left corner of the center tile
        xp _ int(width / 2 - (tx - math.floor(tx)) * TDIM)
        yp _ int(height / 2 - (ty - math.floor(ty)) * TDIM)

        # first tile vertical and horizontal
        xa _ (xp + TDIM - 1) / TDIM
        ya _ (yp + TDIM - 1) / TDIM
        xs _ int(tx) - xa
        ys _ int(ty) - ya

        # offset for top-left tile
        _offset _ QPoint(xp - xa * TDIM, yp - ya * TDIM)

        # last tile vertical and horizontal
        xe _ int(tx) + (width - xp - 1) / TDIM
        ye _ int(ty) + (height - yp - 1) / TDIM

        # build a rect
        _tilesRect _ QRect(xs, ys, xe - xs + 1, ye - ys + 1)

        __ _url.isEmpty
            download()

        updated.e..(QRect(0, 0, width, height))

    ___ render  p, rect):
        ___ x __ range(_tilesRect.width()):
            ___ y __ range(_tilesRect.height()):
                tp _ Point(x + _tilesRect.left(), y + _tilesRect.top())
                box _ tileRect(tp)
                __ rect.intersects(box):
                    p.drawPixmap(box, _tilePixmaps.g..(tp, _emptyTile))
   
    ___ pan  delta):
        dx _ QPointF(delta) / float(TDIM)
        center _ tileForCoordinate(latitude, longitude, zoom) - dx
        latitude _ latitudeFromTile(center.y(), zoom)
        longitude _ longitudeFromTile(center.x(), zoom)
        invalidate()

    # slots
    ___ handleNetworkData  reply):
        img _ QImage()
        tp _ Point(reply.request().attribute(QNetworkRequest.User))
        url _ reply.url()
        __ no. reply.error
            __ img.load(reply, N..):
                _tilePixmaps[tp] _ QPixmap.fromImage(img)
        reply.deleteLater()
        updated.e..(tileRect(tp))

        # purge unused tiles
        bound _ _tilesRect.adjusted(-2, -2, 2, 2)
        ___ tp __ list(_tilePixmaps.keys()):
            __ no. bound.contains(tp):
                del _tilePixmaps[tp]
        download()

    ___ download 
        grab _ N..
        ___ x __ range(_tilesRect.width()):
            ___ y __ range(_tilesRect.height()):
                tp _ Point(_tilesRect.topLeft() + QPoint(x, y))
                __ tp no. __ _tilePixmaps:
                    grab _ QPoint(tp)
                    break

        __ grab __ N..:
            _url _ QUrl()
            r_

        path _ 'http://tile.openstreetmap.org/%d/%d/%d.png' % (zoom, grab.x(), grab.y())
        _url _ QUrl(path)
        request _ QNetworkRequest()
        request.setUrl(_url)
        request.setRawHeader(b'User-Agent', b'Nokia (PyQt) Graphics Dojo 1.0')
        request.setAttribute(QNetworkRequest.User, grab)
        _manager.g..(request)

    ___ tileRect  tp):
        t _ tp - _tilesRect.topLeft()
        x _ t.x() * TDIM + _offset.x()
        y _ t.y() * TDIM + _offset.y()

        r_ QRect(x, y, TDIM, TDIM)


c_ LightMaps(?W..):
    ___  -   parent _ N..):
        super(LightMaps, self). - (parent)

        pressed _ False
        snapped _ False
        zoomed _ False
        invert _ False
        _normalMap _ SlippyMap
        _largeMap _ SlippyMap
        pressPos _ QPoint()
        dragPos _ QPoint()
        tapTimer _ QBasicTimer()
        zoomPixmap _ QPixmap()
        maskPixmap _ QPixmap()
        _normalMap.updated.c..(updateMap)
        _largeMap.updated.c..(update)
 
    ___ setCenter  lat, lng):
        _normalMap.latitude _ lat
        _normalMap.longitude _ lng
        _normalMap.invalidate()
        _largeMap.invalidate()

    # slots
    ___ toggleNightMode 
        invert _ no. invert
        update()
 
    ___ updateMap  r):
        update(r)

    ___ activateZoom 
        zoomed _ True
        tapTimer.stop()
        _largeMap.zoom _ _normalMap.zoom + 1
        _largeMap.width _ _normalMap.width * 2
        _largeMap.height _ _normalMap.height * 2
        _largeMap.latitude _ _normalMap.latitude
        _largeMap.longitude _ _normalMap.longitude
        _largeMap.invalidate()
        update()
 
    ___ resizeEvent  event):
        _normalMap.width _ width()
        _normalMap.height _ height()
        _normalMap.invalidate()
        _largeMap.width _ _normalMap.width * 2
        _largeMap.height _ _normalMap.height * 2
        _largeMap.invalidate()

    ___ paintEvent  event):
        p _ QPainter()
        p.begin
        _normalMap.render(p, event.rect())
        p.setPen(__.black)
        p.drawText(rect(), __.AlignBottom | __.TextWordWrap,
                   "Map data CCBYSA 2009 OpenStreetMap.org contributors")
        p.end()

        __ zoomed:
            dim _ min(width(), height())
            magnifierSize _ min(MAX_MAGNIFIER, dim * 2 / 3)
            radius _ magnifierSize / 2
            ring _ radius - 15
            box _ ?S..(magnifierSize, magnifierSize)

            # reupdate our mask
            __ maskPixmap.size() !_ box:
                maskPixmap _ QPixmap(box)
                maskPixmap.fill(__.transparent)
                g _ QRadialGradient()
                g.setCenter(radius, radius)
                g.setFocalPoint(radius, radius)
                g.setRadius(radius)
                g.setColorAt(1.0, ?C..(255, 255, 255, 0))
                g.setColorAt(0.5, ?C..(128, 128, 128, 255))
                mask _ QPainter(maskPixmap)
                mask.setRenderHint(QPainter.Antialiasing)
                mask.setCompositionMode(QPainter.CompositionMode_Source)
                mask.setBrush(g)
                mask.setPen(__.NoPen)
                mask.drawRect(maskPixmap.rect())
                mask.setBrush(?C..(__.transparent))
                mask.drawEllipse(g.center(), ring, ring)
                mask.end()

            center _ dragPos - QPoint(0, radius)
            center +_ QPoint(0, radius / 2)
            corner _ center - QPoint(radius, radius)
            xy _ center * 2 - QPoint(radius, radius)
            # only set the dimension to the magnified portion
            __ zoomPixmap.size() !_ box:
                zoomPixmap _ QPixmap(box)
                zoomPixmap.fill(__.lightGray)
    
            __ T..
                p _ QPainter(zoomPixmap)
                p.translate(-xy)
                _largeMap.render(p, QRect(xy, box))
                p.end()

            clipPath _ QPainterPath()
            clipPath.addEllipse(QPointF(center), ring, ring)
            p _ QPainter
            p.setRenderHint(QPainter.Antialiasing)
            p.setClipPath(clipPath)
            p.drawPixmap(corner, zoomPixmap)
            p.setClipping F..
            p.drawPixmap(corner, maskPixmap)
            p.setPen(__.gray)
            p.drawPath(clipPath)

        __ invert:
            p _ QPainter
            p.setCompositionMode(QPainter.CompositionMode_Difference)
            p.fillRect(event.rect(), __.white)
            p.end()

    ___ timerEvent  event):
        __ no. zoomed:
            activateZoom()

        update()
 
    ___ mousePressEvent  event):
        __ event.buttons() !_ __.LeftButton:
            r_

        pressed _ snapped _ True
        pressPos _ dragPos _ event.pos()
        tapTimer.stop()
        tapTimer.start(HOLD_TIME, self)

    ___ mouseMoveEvent  event):
        __ no. event.buttons
            r_

        __ no. zoomed:
            __ no. pressed or no. snapped:
                delta _ event.pos() - pressPos
                pressPos _ event.pos()
                _normalMap.pan(delta)
                r_
            ____
                threshold _ 10
                delta _ event.pos() - pressPos
                __ snapped:
                    snapped &_ delta.x() < threshold
                    snapped &_ delta.y() < threshold
                    snapped &_ delta.x() > -threshold
                    snapped &_ delta.y() > -threshold

                __ no. snapped:
                    tapTimer.stop()

        ____
            dragPos _ event.pos()
            update()

    ___ mouseReleaseEvent  event):
        zoomed _ False
        update()
 
    ___ keyPressEvent  event):
        __ no. zoomed:
            __ event.key() == __.Key_Left:
                _normalMap.pan(QPoint(20, 0))
            __ event.key() == __.Key_Right:
                _normalMap.pan(QPoint(-20, 0))
            __ event.key() == __.Key_Up:
                _normalMap.pan(QPoint(0, 20))
            __ event.key() == __.Key_Down:
                _normalMap.pan(QPoint(0, -20))
            __ event.key() == __.Key_Z or event.key() == __.Key_Select:
                dragPos _ QPoint(width() / 2, height() / 2)
                activateZoom()
        ____
            __ event.key() == __.Key_Z or event.key() == __.Key_Select:
                zoomed _ False
                update()

            delta _ QPoint(0, 0)
            __ event.key() == __.Key_Left:
                delta _ QPoint(-15, 0)
            __ event.key() == __.Key_Right:
                delta _ QPoint(15, 0)
            __ event.key() == __.Key_Up:
                delta _ QPoint(0, -15)
            __ event.key() == __.Key_Down:
                delta _ QPoint(0, 15)
            __ delta !_ QPoint(0, 0):
                dragPos +_ delta
                update()


c_ MapZoom ?MW..
    ___  -
        super(MapZoom, self). - (N..)

        map_ _ LightMaps
        sCW..(map_)
        map_.setFocus()
        osloAction _ ?A..("&Oslo", self)
        berlinAction _ ?A..("&Berlin", self)
        jakartaAction _ ?A..("&Jakarta", self)
        nightModeAction _ ?A..("Night Mode", self)
        nightModeAction.setCheckable( st.
        nightModeAction.setChecked F..
        osmAction _ ?A..("About OpenStreetMap", self)
        osloAction.t__.c..(chooseOslo)
        berlinAction.t__.c..(chooseBerlin)
        jakartaAction.t__.c..(chooseJakarta)
        nightModeAction.t__.c..(map_.toggleNightMode)
        osmAction.t__.c..(aboutOsm)

        menu _ mB.. .aM..("&Options")
        menu.aA..(osloAction)
        menu.aA..(berlinAction)
        menu.aA..(jakartaAction)
        menu.addSeparator()
        menu.aA..(nightModeAction)
        menu.aA..(osmAction)

    # slots
    ___ chooseOslo 
        map_.setCenter(59.9138204, 10.7387413)

    ___ chooseBerlin 
        map_.setCenter(52.52958999943302, 13.383053541183472)

    ___ chooseJakarta 
        map_.setCenter(-6.211544, 106.845172)

    ___ aboutOsm 
        QDesktopServices.openUrl(QUrl('http://www.openstreetmap.org'))


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    app.sAN..('LightMaps')
    w _ MapZoom()
    w.sWT..("OpenStreetMap")
    w.r..(600, 450)
    w.s..
    ___.e..(app.exec_())
