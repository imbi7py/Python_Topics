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
        MainWindow.resize(484, 371)
        self.centralWidget _ ?W...QWidget(MainWindow)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Maximum, ?W...QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout _ ?W...QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout _ ?W...QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistView _ ?W...QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(?W...QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout.addWidget(self.playlistView)
        self.horizontalLayout_4 _ ?W...QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeLabel _ ?W...QLabel(self.centralWidget)
        self.currentTimeLabel.setMinimumSize(?C...QSize(80, 0))
        self.currentTimeLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout_4.addWidget(self.currentTimeLabel)
        self.timeSlider _ ?W...QSlider(self.centralWidget)
        self.timeSlider.setOrientation(?C...__.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)
        self.totalTimeLabel _ ?W...QLabel(self.centralWidget)
        self.totalTimeLabel.setMinimumSize(?C...QSize(80, 0))
        self.totalTimeLabel.setAlignment(?C...__.AlignLeading|?C...__.AlignLeft|?C...__.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout_4.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 _ ?W...QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.previousButton _ ?W...?PB..(self.centralWidget)
        self.previousButton.sT..("")
        icon _ ?G...QIcon()
        icon.addPixmap(?G...QPixmap("images/control-skip-180.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)
        self.playButton _ ?W...?PB..(self.centralWidget)
        self.playButton.sT..("")
        icon1 _ ?G...QIcon()
        icon1.addPixmap(?G...QPixmap("images/control.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)
        self.pauseButton _ ?W...?PB..(self.centralWidget)
        self.pauseButton.sT..("")
        icon2 _ ?G...QIcon()
        icon2.addPixmap(?G...QPixmap("images/control-pause.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.stopButton _ ?W...?PB..(self.centralWidget)
        self.stopButton.sT..("")
        icon3 _ ?G...QIcon()
        icon3.addPixmap(?G...QPixmap("images/control-stop-square.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)
        self.nextButton _ ?W...?PB..(self.centralWidget)
        self.nextButton.sT..("")
        icon4 _ ?G...QIcon()
        icon4.addPixmap(?G...QPixmap("images/control-skip.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        self.viewButton _ ?W...?PB..(self.centralWidget)
        self.viewButton.sT..("")
        icon5 _ ?G...QIcon()
        icon5.addPixmap(?G...QPixmap("images/application-image.png"), ?G...QIcon.Normal, ?G...QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(True)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)
        spacerItem _ ?W...QSpacerItem(40, 20, ?W...QSizePolicy.Expanding, ?W...QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label _ ?W...QLabel(self.centralWidget)
        self.label.sT..("")
        self.label.setPixmap(?G...QPixmap("images/speaker-volume.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.volumeSlider _ ?W...QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(?C...__.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.sCW..(self.centralWidget)
        self.menuBar _ ?W...QMenuBar(MainWindow)
        self.menuBar.setGeometry(?C...QRect(0, 0, 484, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFIle _ ?W...QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar _ ?W...QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.open_file_action _ ?W...?A..(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.menuFIle.aA..(self.open_file_action)
        self.menuBar.aA..(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C...QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Failamp"))
        self.currentTimeLabel.sT..(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.sT..(_translate("MainWindow", "0:00"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.open_file_action.sT..(_translate("MainWindow", "Open file..."))

