# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagesettings.ui'
#
# Created: Fri Jun 28 11:48:28 2013
#      by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_ImageSettingsUi(object):
    ___ setupUi  ImageSettingsUi):
        ImageSettingsUi.setObjectName("ImageSettingsUi")
        ImageSettingsUi.r..(332, 270)
        gridLayout _ ?W...QGridLayout(ImageSettingsUi)
        gridLayout.setObjectName("gridLayout")
        groupBox_2 _ ?W...QGroupBox(ImageSettingsUi)
        groupBox_2.setObjectName("groupBox_2")
        gridLayout_2 _ ?W...QGridLayout(groupBox_2)
        gridLayout_2.setObjectName("gridLayout_2")
        label_8 _ ?W...QLabel(groupBox_2)
        label_8.setObjectName("label_8")
        gridLayout_2.aW..(label_8, 0, 0, 1, 2)
        imageResolutionBox _ ?W...QComboBox(groupBox_2)
        imageResolutionBox.setObjectName("imageResolutionBox")
        gridLayout_2.aW..(imageResolutionBox, 1, 0, 1, 2)
        label_6 _ ?W...QLabel(groupBox_2)
        label_6.setObjectName("label_6")
        gridLayout_2.aW..(label_6, 2, 0, 1, 2)
        imageCodecBox _ ?W...QComboBox(groupBox_2)
        imageCodecBox.setObjectName("imageCodecBox")
        gridLayout_2.aW..(imageCodecBox, 3, 0, 1, 2)
        label_7 _ ?W...QLabel(groupBox_2)
        label_7.setObjectName("label_7")
        gridLayout_2.aW..(label_7, 4, 0, 1, 1)
        imageQualitySlider _ ?W...QSlider(groupBox_2)
        imageQualitySlider.setMaximum(4)
        imageQualitySlider.setOrientation(?C...__.Horizontal)
        imageQualitySlider.setObjectName("imageQualitySlider")
        gridLayout_2.aW..(imageQualitySlider, 4, 1, 1, 1)
        gridLayout.aW..(groupBox_2, 0, 0, 1, 1)
        spacerItem _ ?W...QSpacerItem(20, 14, ?W...QSizePolicy.Minimum, ?W...QSizePolicy.E..)
        gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        buttonBox _ ?W...QDialogButtonBox(ImageSettingsUi)
        buttonBox.setOrientation(?C...__.Horizontal)
        buttonBox.setStandardButtons(?W...QDialogButtonBox.Cancel|?W...QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.aW..(buttonBox, 2, 0, 1, 1)

        retranslateUi(ImageSettingsUi)
        buttonBox.accepted.c..(ImageSettingsUi.accept)
        buttonBox.rejected.c..(ImageSettingsUi.reject)
        ?C...QMetaObject.connectSlotsByName(ImageSettingsUi)

    ___ retranslateUi  ImageSettingsUi):
        _translate _ ?C...QCoreApplication.translate
        ImageSettingsUi.sWT..(_translate("ImageSettingsUi", "Dialog"))
        groupBox_2.setTitle(_translate("ImageSettingsUi", "Image"))
        label_8.sT..(_translate("ImageSettingsUi", "Resolution:"))
        label_6.sT..(_translate("ImageSettingsUi", "Image Format:"))
        label_7.sT..(_translate("ImageSettingsUi", "Quality:"))

