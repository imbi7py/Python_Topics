# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week2\projectManager\widgets\projectManager.ui'
#
# Created: Thu Oct 09 13:24:16 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

____ PyQt4 _____ ?C.., ?G..

try:
    _fromUtf8 _ ?C...QString.fromUtf8
except AttributeError:
    ___ _fromUtf8(s
        return s

try:
    _encoding _ ?G...?A...UnicodeUTF8
    ___ _translate(context, t.., disambig
        return ?G...?A...translate(context, t.., disambig, _encoding)
except AttributeError:
    ___ _translate(context, t.., disambig
        return ?G...?A...translate(context, t.., disambig)

c_ Ui_projectManager(object
    ___ setupUi , projectManager
        projectManager.setObjectName(_fromUtf8("projectManager"))
        projectManager.resize(508, 384)
        centralwidget _ ?G...?W..(projectManager)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
        verticalLayout_2 _ ?G...QVBoxLayout(centralwidget)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        splitter _ ?G...QSplitter(centralwidget)
        splitter.setOrientation(?C...Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        verticalLayoutWidget _ ?G...?W..(splitter)
        verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        projectList_ly _ ?G...QVBoxLayout(verticalLayoutWidget)
        projectList_ly.setMargin(0)
        projectList_ly.setObjectName(_fromUtf8("projectList_ly"))
        widget _ ?G...?W..(splitter)
        widget.setObjectName(_fromUtf8("widget"))
        verticalLayout _ ?G...QVBoxLayout(widget)
        verticalLayout.setMargin(0)
        verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        create_btn _ ?G...?PB..(widget)
        create_btn.setObjectName(_fromUtf8("create_btn"))
        verticalLayout.addWidget(create_btn)
        templateEditor_btn _ ?G...?PB..(widget)
        templateEditor_btn.setObjectName(_fromUtf8("templateEditor_btn"))
        verticalLayout.addWidget(templateEditor_btn)
        groupBox _ ?G...QGroupBox(widget)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        verticalLayout_3 _ ?G...QVBoxLayout(groupBox)
        verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        info_lb _ ?G...QLabel(groupBox)
        info_lb.setAlignment(?C...Qt.AlignLeading|?C...Qt.AlignLeft|?C...Qt.AlignTop)
        info_lb.setObjectName(_fromUtf8("info_lb"))
        verticalLayout_3.addWidget(info_lb)
        verticalLayout.addWidget(groupBox)
        settings_btn _ ?G...?PB..(widget)
        settings_btn.setObjectName(_fromUtf8("settings_btn"))
        verticalLayout.addWidget(settings_btn)
        verticalLayout_2.addWidget(splitter)
        projectManager.setCentralWidget(centralwidget)

        retranslateUi(projectManager)
        ?C...QMetaObject.connectSlotsByName(projectManager)

    ___ retranslateUi , projectManager
        projectManager.setWindowTitle(_translate("projectManager", "Project Manager", None))
        create_btn.sT..(_translate("projectManager", "Create Project", None))
        templateEditor_btn.sT..(_translate("projectManager", "Template Editor", None))
        groupBox.setTitle(_translate("projectManager", "Info", None))
        info_lb.sT..(_translate("projectManager", "TextLabel", None))
        settings_btn.sT..(_translate("projectManager", "Settings", None))

