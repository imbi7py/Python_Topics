# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow(object):
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(484, 371)
        centralWidget _ ?W...?W..(MainWindow)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Maximum, ?W...QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centralWidget.sizePolicy().hasHeightForWidth())
        centralWidget.sSP..(sizePolicy)
        centralWidget.setObjectName("centralWidget")
        horizontalLayout _ ?W...QHBoxLayout(centralWidget)
        horizontalLayout.setContentsMargins(11, 11, 11, 11)
        horizontalLayout.setSpacing(6)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout _ ?W...?VBL..
        verticalLayout.setSpacing(6)
        verticalLayout.setObjectName("verticalLayout")
        playlistView _ ?W...QListView(centralWidget)
        playlistView.setAcceptDrops( st.
        playlistView.setProperty("showDropIndicator",  st.
        playlistView.setDragDropMode(?W...QAbstractItemView.DropOnly)
        playlistView.setAlternatingRowColors( st.
        playlistView.setUniformItemSizes( st.
        playlistView.setObjectName("playlistView")
        verticalLayout.aW..(playlistView)
        horizontalLayout_4 _ ?W...?HBL..
        horizontalLayout_4.setSpacing(6)
        horizontalLayout_4.setObjectName("horizontalLayout_4")
        currentTimeLabel _ ?W...QLabel(centralWidget)
        currentTimeLabel.sMS..(?C...?S..(80, 0))
        currentTimeLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        currentTimeLabel.setObjectName("currentTimeLabel")
        horizontalLayout_4.aW..(currentTimeLabel)
        timeSlider _ ?W...?S..(centralWidget)
        timeSlider.setOrientation(?C...__.H..)
        timeSlider.setObjectName("timeSlider")
        horizontalLayout_4.aW..(timeSlider)
        totalTimeLabel _ ?W...QLabel(centralWidget)
        totalTimeLabel.sMS..(?C...?S..(80, 0))
        totalTimeLabel.setAlignment(?C...__.AlignLeading|?C...__.AlignLeft|?C...__.AlignVCenter)
        totalTimeLabel.setObjectName("totalTimeLabel")
        horizontalLayout_4.aW..(totalTimeLabel)
        verticalLayout.aL..(horizontalLayout_4)
        horizontalLayout_5 _ ?W...?HBL..
        horizontalLayout_5.setSpacing(6)
        horizontalLayout_5.setObjectName("horizontalLayout_5")
        previousButton _ ?W...?PB..(centralWidget)
        previousButton.sT..("")
        icon _ ?G...?I..
        icon.aP..(?G...?P..("images/control-skip-180.png"), ?G...?I...Normal, ?G...?I...Off)
        previousButton.sI..(icon)
        previousButton.setObjectName("previousButton")
        horizontalLayout_5.aW..(previousButton)
        playButton _ ?W...?PB..(centralWidget)
        playButton.sT..("")
        icon1 _ ?G...?I..
        icon1.aP..(?G...?P..("images/control.png"), ?G...?I...Normal, ?G...?I...Off)
        playButton.sI..(icon1)
        playButton.setObjectName("playButton")
        horizontalLayout_5.aW..(playButton)
        pauseButton _ ?W...?PB..(centralWidget)
        pauseButton.sT..("")
        icon2 _ ?G...?I..
        icon2.aP..(?G...?P..("images/control-pause.png"), ?G...?I...Normal, ?G...?I...Off)
        pauseButton.sI..(icon2)
        pauseButton.setObjectName("pauseButton")
        horizontalLayout_5.aW..(pauseButton)
        stopButton _ ?W...?PB..(centralWidget)
        stopButton.sT..("")
        icon3 _ ?G...?I..
        icon3.aP..(?G...?P..("images/control-stop-square.png"), ?G...?I...Normal, ?G...?I...Off)
        stopButton.sI..(icon3)
        stopButton.setObjectName("stopButton")
        horizontalLayout_5.aW..(stopButton)
        nextButton _ ?W...?PB..(centralWidget)
        nextButton.sT..("")
        icon4 _ ?G...?I..
        icon4.aP..(?G...?P..("images/control-skip.png"), ?G...?I...Normal, ?G...?I...Off)
        nextButton.sI..(icon4)
        nextButton.setObjectName("nextButton")
        horizontalLayout_5.aW..(nextButton)
        viewButton _ ?W...?PB..(centralWidget)
        viewButton.sT..("")
        icon5 _ ?G...?I..
        icon5.aP..(?G...?P..("images/application-image.png"), ?G...?I...Normal, ?G...?I...Off)
        viewButton.sI..(icon5)
        viewButton.setCheckable( st.
        viewButton.setObjectName("viewButton")
        horizontalLayout_5.aW..(viewButton)
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.E.., ?W...QSizePolicy.Minimum)
        horizontalLayout_5.aI..(spacerItem)
        label _ ?W...QLabel(centralWidget)
        label.sT..("")
        label.sP..(?G...?P..("images/speaker-volume.png"))
        label.setObjectName("label")
        horizontalLayout_5.aW..(label)
        volumeSlider _ ?W...?S..(centralWidget)
        volumeSlider.sM..(100)
        volumeSlider.setProperty("value", 100)
        volumeSlider.setOrientation(?C...__.H..)
        volumeSlider.setObjectName("volumeSlider")
        horizontalLayout_5.aW..(volumeSlider)
        verticalLayout.aL..(horizontalLayout_5)
        horizontalLayout.aL..(verticalLayout)
        MainWindow.sCW..(centralWidget)
        menuBar _ ?W...QMenuBar(MainWindow)
        menuBar.setGeometry(?C...QRect(0, 0, 484, 22))
        menuBar.setObjectName("menuBar")
        menuFIle _ ?W...QMenu(menuBar)
        menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(menuBar)
        statusBar _ ?W...QStatusBar(MainWindow)
        statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(statusBar)
        open_file_action _ ?W...?A..(MainWindow)
        open_file_action.setObjectName("open_file_action")
        menuFIle.aA..(open_file_action)
        menuBar.aA..(menuFIle.menuAction())

        retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Failamp"))
        currentTimeLabel.sT..(_translate("MainWindow", "0:00"))
        totalTimeLabel.sT..(_translate("MainWindow", "0:00"))
        menuFIle.setTitle(_translate("MainWindow", "FIle"))
        open_file_action.sT..(_translate("MainWindow", "Open file..."))

