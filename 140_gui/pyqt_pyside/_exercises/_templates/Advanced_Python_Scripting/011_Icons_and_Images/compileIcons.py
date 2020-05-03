_____ ___
_____ os
____ PySide.?C.. _____ _
____ PySide.?G.. _____ _

c_ fileListClass(QListWidget
    ___  -  , parent
        super(fileListClass, self). - (parent)
        setAcceptDrops(T..)
        pathList _ []

    ___ appendImage , path
        path _ path.replace('/', '\\')
        __ not path __ pathList:
            name _ os.path.basename(path)
            item _ ?LWI..
            item.sT..(name)
            item.setData(32, path)
            aI..(item)
            pathList.ap..(path)

    ___ dragEnterEvent , event
        __ event.mimeData.hasUrls(
            event.accept
        ____
            event.ignore

    ___ dragMoveEvent , event
        __ event.mimeData.hasUrls(
            event.accept
        ____
            event.ignore

c_ resourceCompileClass(QMainWindow
    ___  -
        super(resourceCompileClass, self). - 
        setWindowTitle('Resource Compiler')
        resize(250, 300)
        w _ ?W..
        setCentralWidget(w)
        ly _ QVBoxLayout
        w.setLayout(ly)
        list _ fileListClass
        ly.addWidget(list)
        run_btn _ ?PB..('RUN')
        ly.addWidget(run_btn)
        run_btn.c___.c..(runCompile)
        __ le. __ 2:
            image _ ___.argv[1]
            list.appendImage(image)

    ___ compileQrc , qrc
        workDir _ os.path.dirname(qrc)
        os.chdir(workDir)
        # PySide
        compliled _ os.path.join(os.path.dirname(qrc), 'icons_rcs.py')
        rcc _ 'C:/Python27/Lib/site-packages/PySide/pyside-rcc.exe'
        cmd _ ' '.join([rcc, qrc, 'o', compliled])
        os.system(cmd)
        # PyQt
        compliled _ os.path.join(os.path.dirname(qrc), 'icons_rc.py')
        rcc _ 'C:/Python27/Lib/site-packages/PyQt4/pyrcc.exe'
        cmd _ ' '.join([rcc, qrc, 'o', compliled])
        os.system(cmd)
        r_ T..

    ___ runCompile
        files _ [list.item(i).data(32) ___ i in range(list.count())]
        qrc _ os.path.join(os.path.dirname(files[0]), 'recource.qrc')
        __ writeFile(qrc, files
            compileQrc(qrc)

    ___ writeFile , qrc, files
        w__ o..(qrc, 'w') __ f:
            f.w..('<RCC>\n\t<qresource>\n')
            ___ ico in files:
                f.w..('\t\t<file>%s</file>\n' % os.path.basename(ico))
            f.w..('\t</qresource>\n</RCC>/')
        r_ T..

app _ ?A..