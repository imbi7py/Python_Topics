# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 391)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 221, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 51, 41))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(130, 160, 521, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 731, 311))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 20, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 70, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 70, 61, 51))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar_2.setGeometry(QtCore.QRect(130, 170, 491, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 220, 211, 32))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(160, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(290, 130, 281, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 20, 61, 51))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 60, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 60, 51, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(33, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_3.setGeometry(QtCore.QRect(120, 200, 511, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 110, 211, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 240, 201, 32))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(330, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Euphemia UCAS")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 160, 41, 21))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_4)
        self.lcdNumber_2.setGeometry(QtCore.QRect(500, 160, 41, 21))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter download link here"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "use browse button to enter save location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter video URL"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "User browse button for save location"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Download"))
        self.label.setText(_translate("MainWindow", "Video Quality"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "One Video"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter Playlist URL"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Use browse button to enter save location"))
        self.label_2.setText(_translate("MainWindow", "Video Quality"))
        self.pushButton_7.setText(_translate("MainWindow", "Start Download"))
        self.label_3.setText(_translate("MainWindow", "The Current Video :"))
        self.label_4.setText(_translate("MainWindow", "The Full Playlist Video : "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Full Playlist"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

import photo_rc