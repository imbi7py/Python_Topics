_____ ___
_____ os
____ PySide.?C.. _____ *
____ PySide.?G.. _____ *


c_ listWidgetClass(QListWidget
    ___  -  
        super(listWidgetClass, self). - ()
        setWindowFlags(Qt.WindowStaysOnTopHint)
        setDragDropMode(QAbstractItemView.DropOnly)

    ___ dropEvent , event
        print 'DROP', type(event)
    #     mimedata = event.mimeData()
    #     if mimedata.hasText():
    #         print 'text'
    #         # print mimedata.hasText()
    #     elif mimedata.hasUrls():
    #         print 'urls'
    #         # print mimedata.urls()
    #
    ___ dragEnterEvent , event
        event.accept()
        print 'ENTER', type(event)

    ___ dragMoveEvent , event
        event.accept()
        # print 'MOVE'


__ __name__ __ '__main__':
    _____ ___

    app _ None
    try:
        _____ nuke
    except ImportError:
        app _ ?A..(___.argv)
    main _ listWidgetClass()
    main.s..

    __ app is not None:
        app.exec_()