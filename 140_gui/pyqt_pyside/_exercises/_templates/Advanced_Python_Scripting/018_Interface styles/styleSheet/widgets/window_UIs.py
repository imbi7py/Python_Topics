# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week7\styleSheet\widgets\window.ui'
#
# Created: Wed Nov 12 22:08:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., ?G..

c_ Ui_MainWindow(object
    ___ setupUi , MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 411)
        centralwidget _ ?G...?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        verticalLayout _ ?G...QVBoxLayout(centralwidget)
        verticalLayout.setObjectName("verticalLayout")
        lineEdit _ ?G...QLineEdit(centralwidget)
        lineEdit.setObjectName("lineEdit")
        verticalLayout.addWidget(lineEdit)
        pushButton _ ?G...?PB..(centralwidget)
        pushButton.setObjectName("pushButton")
        verticalLayout.addWidget(pushButton)
        horizontalSlider _ ?G...QSlider(centralwidget)
        horizontalSlider.setMaximum(100)
        horizontalSlider.setOrientation(?C...Qt.Horizontal)
        horizontalSlider.setObjectName("horizontalSlider")
        verticalLayout.addWidget(horizontalSlider)
        checkBox _ ?G...QCheckBox(centralwidget)
        checkBox.setObjectName("checkBox")
        verticalLayout.addWidget(checkBox)
        horizontalLayout_2 _ ?G...QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        radioButton_2 _ ?G...QRadioButton(centralwidget)
        radioButton_2.setChecked(T..)
        radioButton_2.setObjectName("radioButton_2")
        horizontalLayout_2.addWidget(radioButton_2)
        radioButton _ ?G...QRadioButton(centralwidget)
        radioButton.setObjectName("radioButton")
        horizontalLayout_2.addWidget(radioButton)
        spacerItem _ ?G...QSpacerItem(40, 20, ?G...QSizePolicy.Expanding, ?G...QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem)
        verticalLayout.addLayout(horizontalLayout_2)
        treeWidget _ ?G...QTreeWidget(centralwidget)
        treeWidget.setObjectName("treeWidget")
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_2 _ ?G...QTreeWidgetItem(item_1)
        item_3 _ ?G...QTreeWidgetItem(item_2)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_0 _ ?G...QTreeWidgetItem(treeWidget)
        item_1 _ ?G...QTreeWidgetItem(item_0)
        verticalLayout.addWidget(treeWidget)
        comboBox _ ?G...QComboBox(centralwidget)
        comboBox.setObjectName("comboBox")
        comboBox.aI..("")
        comboBox.aI..("")
        comboBox.aI..("")
        comboBox.aI..("")
        comboBox.aI..("")
        verticalLayout.addWidget(comboBox)
        horizontalLayout _ ?G...QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        spinBox _ ?G...QSpinBox(centralwidget)
        spinBox.setMaximum(100)
        spinBox.setObjectName("spinBox")
        horizontalLayout.addWidget(spinBox)
        progressBar _ ?G...QProgressBar(centralwidget)
        progressBar.setProperty("value", 24)
        progressBar.setObjectName("progressBar")
        horizontalLayout.addWidget(progressBar)
        verticalLayout.addLayout(horizontalLayout)
        MainWindow.setCentralWidget(centralwidget)
        menubar _ ?G...QMenuBar(MainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 356, 21))
        menubar.setObjectName("menubar")
        menuFile _ ?G...QMenu(menubar)
        menuFile.setObjectName("menuFile")
        menuOpen _ ?G...QMenu(menuFile)
        menuOpen.setObjectName("menuOpen")
        menuHelop _ ?G...QMenu(menubar)
        menuHelop.setObjectName("menuHelop")
        MainWindow.setMenuBar(menubar)
        actionClose _ ?G...QAction(MainWindow)
        actionClose.setObjectName("actionClose")
        actionExit _ ?G...QAction(MainWindow)
        actionExit.setObjectName("actionExit")
        actionAbout _ ?G...QAction(MainWindow)
        actionAbout.setObjectName("actionAbout")
        actionFile _ ?G...QAction(MainWindow)
        actionFile.setObjectName("actionFile")
        actionProject _ ?G...QAction(MainWindow)
        actionProject.setObjectName("actionProject")
        menuOpen.addAction(actionFile)
        menuOpen.addAction(actionProject)
        menuFile.addAction(menuOpen.menuAction())
        menuFile.addAction(actionClose)
        menuFile.addAction(actionExit)
        menuHelop.addAction(actionAbout)
        menubar.addAction(menuFile.menuAction())
        menubar.addAction(menuHelop.menuAction())

        retranslateUi(MainWindow)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL("valueChanged(int)"), progressBar.setValue)
        ?C...QObject.c..(horizontalSlider, ?C...SIGNAL("valueChanged(int)"), spinBox.setValue)
        ?C...QObject.c..(spinBox, ?C...SIGNAL("valueChanged(int)"), horizontalSlider.setValue)
        ?C...QObject.c..(spinBox, ?C...SIGNAL("valueChanged(int)"), progressBar.setValue)
        ?C...QObject.c..(radioButton_2, ?C...SIGNAL("toggled(bool)"), treeWidget.setEnabled)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi , MainWindow
        MainWindow.setWindowTitle(?G...?A...translate("MainWindow", "MainWindow", None, ?G...?A...UnicodeUTF8))
        pushButton.sT..(?G...?A...translate("MainWindow", "Start", None, ?G...?A...UnicodeUTF8))
        checkBox.sT..(?G...?A...translate("MainWindow", "Show", None, ?G...?A...UnicodeUTF8))
        radioButton_2.sT..(?G...?A...translate("MainWindow", "Enable", None, ?G...?A...UnicodeUTF8))
        radioButton.sT..(?G...?A...translate("MainWindow", "Disable", None, ?G...?A...UnicodeUTF8))
        treeWidget.headerItem().sT..(0, ?G...?A...translate("MainWindow", "1", None, ?G...?A...UnicodeUTF8))
        __sortingEnabled _ treeWidget.isSortingEnabled()
        treeWidget.setSortingEnabled(False)
        treeWidget.topLevelItem(0).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(0).child(0).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(1).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(0).child(2).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(1).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(2).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(3).sT..(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        treeWidget.topLevelItem(3).child(0).sT..(0, ?G...?A...translate("MainWindow", "New Subitem", None, ?G...?A...UnicodeUTF8))
        treeWidget.setSortingEnabled(__sortingEnabled)
        comboBox.setItemText(0, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        comboBox.setItemText(1, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        comboBox.setItemText(2, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        comboBox.setItemText(3, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        comboBox.setItemText(4, ?G...?A...translate("MainWindow", "New Item", None, ?G...?A...UnicodeUTF8))
        menuFile.setTitle(?G...?A...translate("MainWindow", "File", None, ?G...?A...UnicodeUTF8))
        menuOpen.setTitle(?G...?A...translate("MainWindow", "Open", None, ?G...?A...UnicodeUTF8))
        menuHelop.setTitle(?G...?A...translate("MainWindow", "Help", None, ?G...?A...UnicodeUTF8))
        actionClose.sT..(?G...?A...translate("MainWindow", "Close", None, ?G...?A...UnicodeUTF8))
        actionExit.sT..(?G...?A...translate("MainWindow", "Exit", None, ?G...?A...UnicodeUTF8))
        actionAbout.sT..(?G...?A...translate("MainWindow", "About", None, ?G...?A...UnicodeUTF8))
        actionFile.sT..(?G...?A...translate("MainWindow", "File", None, ?G...?A...UnicodeUTF8))
        actionProject.sT..(?G...?A...translate("MainWindow", "Project", None, ?G...?A...UnicodeUTF8))

