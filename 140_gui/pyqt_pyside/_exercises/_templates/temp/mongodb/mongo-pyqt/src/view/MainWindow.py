# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat Oct 25 13:40:24 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, ?W..

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 852)
        self.centralwidget = ?W...?W..(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = ?W...?SP..(?W...?SP...Preferred, ?W...?SP...Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = ?W...?VBL..(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_main = ?W...?VBL..()
        self.verticalLayout_main.setSizeConstraint(?W...QLayout.SetMaximumSize)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.horizontall_up = ?W...?HBL..()
        self.horizontall_up.setObjectName("horizontall_up")
        self.label = ?W...QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontall_up.aW..(self.label)
        self.mongoHost = ?W...QLineEdit(self.centralwidget)
        self.mongoHost.setObjectName("mongoHost")
        self.horizontall_up.aW..(self.mongoHost)
        self.connectBtn = ?W...?PB..(self.centralwidget)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontall_up.aW..(self.connectBtn)
        spacerItem = ?W...?SI..(40, 20, ?W...?SP...Expanding, ?W...?SP...Minimum)
        self.horizontall_up.aI..(spacerItem)
        self.verticalLayout_main.addLayout(self.horizontall_up)
        self.horizontalLayout = ?W...?HBL..()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview1 = ?W...QLabel(self.centralwidget)
        self.preview1.setObjectName("preview1")
        self.horizontalLayout.aW..(self.preview1)
        self.preview = ?W...QLineEdit(self.centralwidget)
        self.preview.sRO..(True)
        self.preview.setObjectName("preview")
        self.horizontalLayout.aW..(self.preview)
        self.querytime = ?W...QLabel(self.centralwidget)
        self.querytime.setMinimumSize(QtCore.QSize(200, 0))
        self.querytime.setText("")
        self.querytime.setObjectName("querytime")
        self.horizontalLayout.aW..(self.querytime)
        self.verticalLayout_main.addLayout(self.horizontalLayout)
        self.horizontal_down = ?W...?HBL..()
        self.horizontal_down.setObjectName("horizontal_down")
        self.treeWidget = ?W...QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.treeWidget.setObjectName("treeWidget")
        self.horizontal_down.aW..(self.treeWidget)
        self.verticall_down_right = ?W...?VBL..()
        self.verticall_down_right.setObjectName("verticall_down_right")
        self.horizontalLayout_2 = ?W...?HBL..()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.query = ?W...QLineEdit(self.centralwidget)
        self.query.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.query.setText("")
        self.query.setClearButtonEnabled(True)
        self.query.setObjectName("query")
        self.horizontalLayout_2.aW..(self.query)
        self.label_2 = ?W...QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.aW..(self.label_2)
        self.sort = ?W...QLineEdit(self.centralwidget)
        sizePolicy = ?W...?SP..(?W...?SP...Minimum, ?W...?SP...Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort.sizePolicy().hasHeightForWidth())
        self.sort.setSizePolicy(sizePolicy)
        self.sort.setMinimumSize(QtCore.QSize(100, 0))
        self.sort.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sort.setText("")
        self.sort.setClearButtonEnabled(False)
        self.sort.setObjectName("sort")
        self.horizontalLayout_2.aW..(self.sort)
        self.querybtn = ?W...?PB..(self.centralwidget)
        self.querybtn.setObjectName("querybtn")
        self.horizontalLayout_2.aW..(self.querybtn)
        self.verticall_down_right.addLayout(self.horizontalLayout_2)
        self.viewDetailLabel = ?W...QLabel(self.centralwidget)
        self.viewDetailLabel.setObjectName("viewDetailLabel")
        self.verticall_down_right.aW..(self.viewDetailLabel)
        self.tableview = ?W...QTableView(self.centralwidget)
        self.tableview.setObjectName("tableview")
        self.verticall_down_right.aW..(self.tableview)
        self.paginationLayoutDown = ?W...?HBL..()
        self.paginationLayoutDown.setObjectName("paginationLayoutDown")
        self.paginationinfo = ?W...QLabel(self.centralwidget)
        self.paginationinfo.setText("")
        self.paginationinfo.setObjectName("paginationinfo")
        self.paginationLayoutDown.aW..(self.paginationinfo)
        self.prevBtn = ?W...?PB..(self.centralwidget)
        self.prevBtn.setEnabled(False)
        self.prevBtn.setMinimumSize(QtCore.QSize(100, 0))
        self.prevBtn.setMaximumSize(QtCore.QSize(100, 100))
        self.prevBtn.setCheckable(False)
        self.prevBtn.setAutoDefault(False)
        self.prevBtn.setDefault(False)
        self.prevBtn.setFlat(False)
        self.prevBtn.setObjectName("prevBtn")
        self.paginationLayoutDown.aW..(self.prevBtn)
        self.nextBtn = ?W...?PB..(self.centralwidget)
        self.nextBtn.setEnabled(False)
        self.nextBtn.setMinimumSize(QtCore.QSize(100, 32))
        self.nextBtn.setMaximumSize(QtCore.QSize(100, 100))
        self.nextBtn.setObjectName("nextBtn")
        self.paginationLayoutDown.aW..(self.nextBtn)
        self.verticall_down_right.addLayout(self.paginationLayoutDown)
        self.horizontal_down.addLayout(self.verticall_down_right)
        self.verticalLayout_main.addLayout(self.horizontal_down)
        self.verticalLayout_5.addLayout(self.verticalLayout_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = ?W...QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = ?W...QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mongo-pyqt"))
        self.label.setText(_translate("MainWindow", "mongo host:"))
        self.connectBtn.setText(_translate("MainWindow", "connect"))
        self.preview1.setText(_translate("MainWindow", "Preview"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "DB"))
        self.query.setPlaceholderText(_translate("MainWindow", "{}"))
        self.label_2.setText(_translate("MainWindow", "sort"))
        self.sort.setPlaceholderText(_translate("MainWindow", "{\"field\":1}"))
        self.querybtn.setText(_translate("MainWindow", "query"))
        self.viewDetailLabel.setText(_translate("MainWindow", "Table Detail:"))
        self.prevBtn.setText(_translate("MainWindow", "Prev"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))

