# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\computeArea\computeArea.ui'
#
# Created: Sun Nov 05 16:17:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

____ PySide _____ ?C.., ?G..

c_ Ui_computeArea(object
    ___ setupUi , computeArea
        computeArea.setObjectName("computeArea")
        computeArea.resize(741, 777)
        centralwidget _ ?G...?W..(computeArea)
        centralwidget.setObjectName("centralwidget")
        verticalLayout_3 _ ?G...QVBoxLayout(centralwidget)
        verticalLayout_3.setObjectName("verticalLayout_3")
        groupBox _ ?G...QGroupBox(centralwidget)
        groupBox.setObjectName("groupBox")
        verticalLayout _ ?G...QVBoxLayout(groupBox)
        verticalLayout.setObjectName("verticalLayout")
        shape_cbb _ ?G...QComboBox(groupBox)
        shape_cbb.setObjectName("shape_cbb")
        shape_cbb.addItem("")
        shape_cbb.addItem("")
        verticalLayout.addWidget(shape_cbb)
        verticalLayout_3.addWidget(groupBox)
        square_gb _ ?G...QGroupBox(centralwidget)
        square_gb.setObjectName("square_gb")
        layoutWidget _ ?G...?W..(square_gb)
        layoutWidget.setGeometry(?C...QRect(30, 30, 401, 101))
        layoutWidget.setObjectName("layoutWidget")
        verticalLayout_2 _ ?G...QVBoxLayout(layoutWidget)
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        verticalLayout_2.setObjectName("verticalLayout_2")
        horizontalLayout _ ?G...QHBoxLayout()
        horizontalLayout.setObjectName("horizontalLayout")
        label _ ?G...QLabel(layoutWidget)
        label.setMinimumSize(?C...QSize(70, 0))
        label.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label.setObjectName("label")
        horizontalLayout.addWidget(label)
        square_height_spx _ ?G...QSpinBox(layoutWidget)
        square_height_spx.setMinimum(1)
        square_height_spx.setMaximum(9999999)
        square_height_spx.setObjectName("square_height_spx")
        horizontalLayout.addWidget(square_height_spx)
        horizontalLayout.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout)
        horizontalLayout_2 _ ?G...QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        label_2 _ ?G...QLabel(layoutWidget)
        label_2.setMinimumSize(?C...QSize(70, 0))
        label_2.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_2.setObjectName("label_2")
        horizontalLayout_2.addWidget(label_2)
        square_width_spx _ ?G...QSpinBox(layoutWidget)
        square_width_spx.setMinimum(10)
        square_width_spx.setMaximum(9999999)
        square_width_spx.setObjectName("square_width_spx")
        horizontalLayout_2.addWidget(square_width_spx)
        horizontalLayout_2.setStretch(1, 1)
        verticalLayout_2.addLayout(horizontalLayout_2)
        verticalLayout_3.addWidget(square_gb)
        circle_gb _ ?G...QGroupBox(centralwidget)
        circle_gb.setObjectName("circle_gb")
        layoutWidget_4 _ ?G...?W..(circle_gb)
        layoutWidget_4.setGeometry(?C...QRect(30, 30, 401, 31))
        layoutWidget_4.setObjectName("layoutWidget_4")
        horizontalLayout_7 _ ?G...QHBoxLayout(layoutWidget_4)
        horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_7.setObjectName("horizontalLayout_7")
        label_7 _ ?G...QLabel(layoutWidget_4)
        label_7.setMinimumSize(?C...QSize(70, 0))
        label_7.setAlignment(?C...Qt.AlignRight|?C...Qt.AlignTrailing|?C...Qt.AlignVCenter)
        label_7.setObjectName("label_7")
        horizontalLayout_7.addWidget(label_7)
        circle_radius_spx _ ?G...QSpinBox(layoutWidget_4)
        circle_radius_spx.setMinimum(1)
        circle_radius_spx.setMaximum(9999999)
        circle_radius_spx.setObjectName("circle_radius_spx")
        horizontalLayout_7.addWidget(circle_radius_spx)
        horizontalLayout_7.setStretch(1, 1)
        verticalLayout_3.addWidget(circle_gb)
        compute_btn _ ?G...?PB..(centralwidget)
        compute_btn.setObjectName("compute_btn")
        verticalLayout_3.addWidget(compute_btn)
        result_lbl _ ?G...QLabel(centralwidget)
        result_lbl.setObjectName("result_lbl")
        verticalLayout_3.addWidget(result_lbl)
        computeArea.setCentralWidget(centralwidget)
        statusbar _ ?G...QStatusBar(computeArea)
        statusbar.setObjectName("statusbar")
        computeArea.setStatusBar(statusbar)

        retranslateUi(computeArea)
        ?C...QMetaObject.connectSlotsByName(computeArea)

    ___ retranslateUi , computeArea
        computeArea.setWindowTitle(?G...?A...translate("computeArea", "ComputeArea", None, ?G...?A...UnicodeUTF8))
        groupBox.setTitle(?G...?A...translate("computeArea", "Select Shape", None, ?G...?A...UnicodeUTF8))
        shape_cbb.setItemText(0, ?G...?A...translate("computeArea", "Square", None, ?G...?A...UnicodeUTF8))
        shape_cbb.setItemText(1, ?G...?A...translate("computeArea", "Radius", None, ?G...?A...UnicodeUTF8))
        square_gb.setTitle(?G...?A...translate("computeArea", "Square", None, ?G...?A...UnicodeUTF8))
        label.sT..(?G...?A...translate("computeArea", "Height", None, ?G...?A...UnicodeUTF8))
        label_2.sT..(?G...?A...translate("computeArea", "Width", None, ?G...?A...UnicodeUTF8))
        circle_gb.setTitle(?G...?A...translate("computeArea", "Circle", None, ?G...?A...UnicodeUTF8))
        label_7.sT..(?G...?A...translate("computeArea", "Radius", None, ?G...?A...UnicodeUTF8))
        compute_btn.sT..(?G...?A...translate("computeArea", "COMPUTE", None, ?G...?A...UnicodeUTF8))
        result_lbl.sT..(?G...?A...translate("computeArea", "Result", None, ?G...?A...UnicodeUTF8))

