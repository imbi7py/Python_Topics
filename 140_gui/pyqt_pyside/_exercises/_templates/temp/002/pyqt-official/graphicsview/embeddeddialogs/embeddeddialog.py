# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'embeddeddialog.ui'
#
# Created: Wed May 15 16:13:29 2013
#      by: PyQt5 UI code generator 5.0-snapshot-8d430da208a7
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_embeddedDialog(object):
    ___ setupUi  embeddedDialog):
        embeddedDialog.setObjectName("embeddedDialog")
        embeddedDialog.r..(407, 134)
        formLayout _ ?W...QFormLayout(embeddedDialog)
        formLayout.setObjectName("formLayout")
        label _ ?W...QLabel(embeddedDialog)
        label.setObjectName("label")
        formLayout.setWidget(0, ?W...QFormLayout.LabelRole, label)
        layoutDirection _ ?W...QComboBox(embeddedDialog)
        layoutDirection.setObjectName("layoutDirection")
        layoutDirection.addItem("")
        layoutDirection.addItem("")
        formLayout.setWidget(0, ?W...QFormLayout.FieldRole, layoutDirection)
        label_2 _ ?W...QLabel(embeddedDialog)
        label_2.setObjectName("label_2")
        formLayout.setWidget(1, ?W...QFormLayout.LabelRole, label_2)
        fontComboBox _ ?W...QFontComboBox(embeddedDialog)
        fontComboBox.setObjectName("fontComboBox")
        formLayout.setWidget(1, ?W...QFormLayout.FieldRole, fontComboBox)
        label_3 _ ?W...QLabel(embeddedDialog)
        label_3.setObjectName("label_3")
        formLayout.setWidget(2, ?W...QFormLayout.LabelRole, label_3)
        style _ ?W...QComboBox(embeddedDialog)
        style.setObjectName("style")
        formLayout.setWidget(2, ?W...QFormLayout.FieldRole, style)
        label_4 _ ?W...QLabel(embeddedDialog)
        label_4.setObjectName("label_4")
        formLayout.setWidget(3, ?W...QFormLayout.LabelRole, label_4)
        spacing _ ?W...QSlider(embeddedDialog)
        spacing.setOrientation(?C...__.Horizontal)
        spacing.setObjectName("spacing")
        formLayout.setWidget(3, ?W...QFormLayout.FieldRole, spacing)
        label.setBuddy(layoutDirection)
        label_2.setBuddy(fontComboBox)
        label_3.setBuddy(style)
        label_4.setBuddy(spacing)

        retranslateUi(embeddedDialog)
        ?C...QMetaObject.connectSlotsByName(embeddedDialog)

    ___ retranslateUi  embeddedDialog):
        _translate _ ?C...QCoreApplication.translate
        embeddedDialog.sWT..(_translate("embeddedDialog", "Embedded Dialog"))
        label.sT..(_translate("embeddedDialog", "Layout Direction:"))
        layoutDirection.setItemText(0, _translate("embeddedDialog", "Left to Right"))
        layoutDirection.setItemText(1, _translate("embeddedDialog", "Right to Left"))
        label_2.sT..(_translate("embeddedDialog", "Select Font:"))
        label_3.sT..(_translate("embeddedDialog", "Style:"))
        label_4.sT..(_translate("embeddedDialog", "Layout spacing:"))

