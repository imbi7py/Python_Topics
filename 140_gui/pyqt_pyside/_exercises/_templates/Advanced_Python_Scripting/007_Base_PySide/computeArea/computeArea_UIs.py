# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\computeArea\computeArea.ui'
#
# Created: Sun Nov 05 16:17:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_computeArea(object):
    def setupUi(self, computeArea):
        computeArea.setObjectName("computeArea")
        computeArea.resize(741, 777)
        self.centralwidget = QtGui.QWidget(computeArea)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shape_cbb = QtGui.QComboBox(self.groupBox)
        self.shape_cbb.setObjectName("shape_cbb")
        self.shape_cbb.addItem("")
        self.shape_cbb.addItem("")
        self.verticalLayout.addWidget(self.shape_cbb)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.square_gb = QtGui.QGroupBox(self.centralwidget)
        self.square_gb.setObjectName("square_gb")
        self.layoutWidget = QtGui.QWidget(self.square_gb)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 401, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.square_height_spx = QtGui.QSpinBox(self.layoutWidget)
        self.square_height_spx.setMinimum(1)
        self.square_height_spx.setMaximum(9999999)
        self.square_height_spx.setObjectName("square_height_spx")
        self.horizontalLayout.addWidget(self.square_height_spx)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.square_width_spx = QtGui.QSpinBox(self.layoutWidget)
        self.square_width_spx.setMinimum(10)
        self.square_width_spx.setMaximum(9999999)
        self.square_width_spx.setObjectName("square_width_spx")
        self.horizontalLayout_2.addWidget(self.square_width_spx)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.square_gb)
        self.circle_gb = QtGui.QGroupBox(self.centralwidget)
        self.circle_gb.setObjectName("circle_gb")
        self.layoutWidget_4 = QtGui.QWidget(self.circle_gb)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 30, 401, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtGui.QLabel(self.layoutWidget_4)
        self.label_7.setMinimumSize(QtCore.QSize(70, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.circle_radius_spx = QtGui.QSpinBox(self.layoutWidget_4)
        self.circle_radius_spx.setMinimum(1)
        self.circle_radius_spx.setMaximum(9999999)
        self.circle_radius_spx.setObjectName("circle_radius_spx")
        self.horizontalLayout_7.addWidget(self.circle_radius_spx)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.circle_gb)
        self.compute_btn = QtGui.QPushButton(self.centralwidget)
        self.compute_btn.setObjectName("compute_btn")
        self.verticalLayout_3.addWidget(self.compute_btn)
        self.result_lbl = QtGui.QLabel(self.centralwidget)
        self.result_lbl.setObjectName("result_lbl")
        self.verticalLayout_3.addWidget(self.result_lbl)
        computeArea.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(computeArea)
        self.statusbar.setObjectName("statusbar")
        computeArea.setStatusBar(self.statusbar)

        self.retranslateUi(computeArea)
        QtCore.QMetaObject.connectSlotsByName(computeArea)

    def retranslateUi(self, computeArea):
        computeArea.setWindowTitle(QtGui.QApplication.translate("computeArea", "ComputeArea", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("computeArea", "Select Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.shape_cbb.setItemText(0, QtGui.QApplication.translate("computeArea", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.shape_cbb.setItemText(1, QtGui.QApplication.translate("computeArea", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.square_gb.setTitle(QtGui.QApplication.translate("computeArea", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("computeArea", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("computeArea", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.circle_gb.setTitle(QtGui.QApplication.translate("computeArea", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("computeArea", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.compute_btn.setText(QtGui.QApplication.translate("computeArea", "COMPUTE", None, QtGui.QApplication.UnicodeUTF8))
        self.result_lbl.setText(QtGui.QApplication.translate("computeArea", "Result", None, QtGui.QApplication.UnicodeUTF8))
