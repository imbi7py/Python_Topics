_____ ___

____ PyQt5.?W.. _____ ?D.., ?A.., QGraphicsScene, QGraphicsPixmapItem
____ PyQt5.?G.. _____ QPixmap
____ demoGraphicsView _____ _

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        scene _ QGraphicsScene
        pixmap_ ?G...QPixmap()
        pixmap.load("bintupic.jpg")
        item_QGraphicsPixmapItem(pixmap)
        scene.aI..(item)
        ui.graphicsView.setScene(scene)

__ _ ____ __ _____
    app _ ?A..(___.argv)
    myapp _ MyForm()
    myapp.s..
    ___.e..(app.e
