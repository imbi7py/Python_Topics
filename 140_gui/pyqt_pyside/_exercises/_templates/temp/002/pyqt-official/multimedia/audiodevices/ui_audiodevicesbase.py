# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audiodevicesbase.ui'
#
# Created: Tue Jun 25 12:31:11 2013
#      by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_AudioDevicesBase(object):
    ___ setupUi  AudioDevicesBase):
        AudioDevicesBase.setObjectName("AudioDevicesBase")
        AudioDevicesBase.resize(679, 598)
        self.centralwidget _ ?W...QWidget(AudioDevicesBase)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout _ ?W...QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea _ ?W...QScrollArea(self.centralwidget)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Expanding, ?W...QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents _ ?W...QWidget()
        self.scrollAreaWidgetContents.setGeometry(?C...QRect(0, 0, 659, 558))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 _ ?W...QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 _ ?W...QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modeLabel _ ?W...QLabel(self.scrollAreaWidgetContents)
        self.modeLabel.setObjectName("modeLabel")
        self.gridLayout_2.addWidget(self.modeLabel, 0, 0, 1, 1)
        self.deviceLabel _ ?W...QLabel(self.scrollAreaWidgetContents)
        self.deviceLabel.setObjectName("deviceLabel")
        self.gridLayout_2.addWidget(self.deviceLabel, 0, 1, 1, 1)
        self.modeBox _ ?W...QComboBox(self.scrollAreaWidgetContents)
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.gridLayout_2.addWidget(self.modeBox, 1, 0, 1, 1)
        self.deviceBox _ ?W...QComboBox(self.scrollAreaWidgetContents)
        self.deviceBox.setObjectName("deviceBox")
        self.gridLayout_2.addWidget(self.deviceBox, 1, 1, 1, 1)
        self.tabWidget _ ?W...QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.testFormatTab _ ?W...QWidget()
        self.testFormatTab.setObjectName("testFormatTab")
        self.gridLayout _ ?W...QGridLayout(self.testFormatTab)
        self.gridLayout.setObjectName("gridLayout")
        self.actualLabel _ ?W...QLabel(self.testFormatTab)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Preferred, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actualLabel.sizePolicy().hasHeightForWidth())
        self.actualLabel.setSizePolicy(sizePolicy)
        self.actualLabel.setFrameShape(?W...QFrame.NoFrame)
        self.actualLabel.setFrameShadow(?W...QFrame.Plain)
        self.actualLabel.setTextFormat(?C...__.RichText)
        self.actualLabel.setAlignment(?C...__.AlignCenter)
        self.actualLabel.setObjectName("actualLabel")
        self.gridLayout.addWidget(self.actualLabel, 0, 1, 1, 1)
        self.nearestLabel _ ?W...QLabel(self.testFormatTab)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Preferred, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nearestLabel.sizePolicy().hasHeightForWidth())
        self.nearestLabel.setSizePolicy(sizePolicy)
        self.nearestLabel.setFrameShape(?W...QFrame.NoFrame)
        self.nearestLabel.setFrameShadow(?W...QFrame.Plain)
        self.nearestLabel.setTextFormat(?C...__.RichText)
        self.nearestLabel.setAlignment(?C...__.AlignCenter)
        self.nearestLabel.setObjectName("nearestLabel")
        self.gridLayout.addWidget(self.nearestLabel, 0, 2, 1, 1)
        self.sampleRateBox _ ?W...QComboBox(self.testFormatTab)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Expanding, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleRateBox.sizePolicy().hasHeightForWidth())
        self.sampleRateBox.setSizePolicy(sizePolicy)
        self.sampleRateBox.setObjectName("sampleRateBox")
        self.gridLayout.addWidget(self.sampleRateBox, 3, 1, 1, 1)
        self.nearestSampleRate _ ?W...QLineEdit(self.testFormatTab)
        self.nearestSampleRate.setEnabled F..
        self.nearestSampleRate.setObjectName("nearestSampleRate")
        self.gridLayout.addWidget(self.nearestSampleRate, 3, 2, 1, 1)
        self.channelsBox _ ?W...QComboBox(self.testFormatTab)
        self.channelsBox.setObjectName("channelsBox")
        self.gridLayout.addWidget(self.channelsBox, 5, 1, 1, 1)
        self.nearestChannel _ ?W...QLineEdit(self.testFormatTab)
        self.nearestChannel.setEnabled F..
        self.nearestChannel.setObjectName("nearestChannel")
        self.gridLayout.addWidget(self.nearestChannel, 5, 2, 1, 1)
        self.sampleSizesBox _ ?W...QComboBox(self.testFormatTab)
        self.sampleSizesBox.setObjectName("sampleSizesBox")
        self.gridLayout.addWidget(self.sampleSizesBox, 9, 1, 1, 1)
        self.nearestSampleSize _ ?W...QLineEdit(self.testFormatTab)
        self.nearestSampleSize.setEnabled F..
        self.nearestSampleSize.setObjectName("nearestSampleSize")
        self.gridLayout.addWidget(self.nearestSampleSize, 9, 2, 1, 1)
        self.endianBox _ ?W...QComboBox(self.testFormatTab)
        self.endianBox.setObjectName("endianBox")
        self.gridLayout.addWidget(self.endianBox, 14, 1, 1, 1)
        self.nearestEndian _ ?W...QLineEdit(self.testFormatTab)
        self.nearestEndian.setEnabled F..
        self.nearestEndian.setObjectName("nearestEndian")
        self.gridLayout.addWidget(self.nearestEndian, 14, 2, 1, 1)
        self.testButton _ ?W...?PB..(self.testFormatTab)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 15, 1, 1, 1)
        self.testResult _ ?W...QLabel(self.testFormatTab)
        self.testResult.sT..("")
        self.testResult.setObjectName("testResult")
        self.gridLayout.addWidget(self.testResult, 15, 2, 1, 1)
        self.actualFreqLabel _ ?W...QLabel(self.testFormatTab)
        self.actualFreqLabel.setObjectName("actualFreqLabel")
        self.gridLayout.addWidget(self.actualFreqLabel, 3, 0, 1, 1)
        self.actualChannelLabel _ ?W...QLabel(self.testFormatTab)
        self.actualChannelLabel.setObjectName("actualChannelLabel")
        self.gridLayout.addWidget(self.actualChannelLabel, 5, 0, 1, 1)
        self.actualSampleSizeLabel _ ?W...QLabel(self.testFormatTab)
        self.actualSampleSizeLabel.setObjectName("actualSampleSizeLabel")
        self.gridLayout.addWidget(self.actualSampleSizeLabel, 9, 0, 1, 1)
        self.actualEndianLabel _ ?W...QLabel(self.testFormatTab)
        self.actualEndianLabel.setObjectName("actualEndianLabel")
        self.gridLayout.addWidget(self.actualEndianLabel, 14, 0, 1, 1)
        self.label _ ?W...QLabel(self.testFormatTab)
        sizePolicy _ ?W...QSizePolicy(?W...QSizePolicy.Preferred, ?W...QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 16, 0, 1, 3)
        self.actualCodecLabel _ ?W...QLabel(self.testFormatTab)
        self.actualCodecLabel.setObjectName("actualCodecLabel")
        self.gridLayout.addWidget(self.actualCodecLabel, 2, 0, 1, 1)
        self.nearestCodec _ ?W...QLineEdit(self.testFormatTab)
        self.nearestCodec.setEnabled F..
        self.nearestCodec.setObjectName("nearestCodec")
        self.gridLayout.addWidget(self.nearestCodec, 2, 2, 1, 1)
        self.codecsBox _ ?W...QComboBox(self.testFormatTab)
        self.codecsBox.setObjectName("codecsBox")
        self.gridLayout.addWidget(self.codecsBox, 2, 1, 1, 1)
        self.actualSampleTypeLabel _ ?W...QLabel(self.testFormatTab)
        self.actualSampleTypeLabel.setObjectName("actualSampleTypeLabel")
        self.gridLayout.addWidget(self.actualSampleTypeLabel, 6, 0, 1, 1)
        self.sampleTypesBox _ ?W...QComboBox(self.testFormatTab)
        self.sampleTypesBox.setObjectName("sampleTypesBox")
        self.gridLayout.addWidget(self.sampleTypesBox, 6, 1, 1, 1)
        self.nearestSampleType _ ?W...QLineEdit(self.testFormatTab)
        self.nearestSampleType.setEnabled F..
        self.nearestSampleType.setObjectName("nearestSampleType")
        self.gridLayout.addWidget(self.nearestSampleType, 6, 2, 1, 1)
        self.tabWidget.addTab(self.testFormatTab, "")
        self.tab _ ?W...QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 _ ?W...QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.populateTableButton _ ?W...?PB..(self.tab)
        self.populateTableButton.setObjectName("populateTableButton")
        self.verticalLayout_2.addWidget(self.populateTableButton)
        self.allFormatsTable _ ?W...QTableWidget(self.tab)
        self.allFormatsTable.setEditTriggers(?W...QAbstractItemView.NoEditTriggers)
        self.allFormatsTable.setDragDropOverwriteMode F..
        self.allFormatsTable.setSelectionMode(?W...QAbstractItemView.NoSelection)
        self.allFormatsTable.setSelectionBehavior(?W...QAbstractItemView.SelectItems)
        self.allFormatsTable.setTextElideMode(?C...__.ElideNone)
        self.allFormatsTable.setWordWrap F..
        self.allFormatsTable.setCornerButtonEnabled F..
        self.allFormatsTable.setObjectName("allFormatsTable")
        self.allFormatsTable.setColumnCount(6)
        self.allFormatsTable.setRowCount(0)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(0, item)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(1, item)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(2, item)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(3, item)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(4, item)
        item _ ?W...QTableWidgetItem()
        item.setTextAlignment(?C...__.AlignHCenter|?C...__.AlignVCenter|?C...__.AlignCenter)
        self.allFormatsTable.setHorizontalHeaderItem(5, item)
        self.allFormatsTable.horizontalHeader().setHighlightSections F..
        self.allFormatsTable.verticalHeader().setVisible F..
        self.allFormatsTable.verticalHeader().setHighlightSections F..
        self.verticalLayout_2.addWidget(self.allFormatsTable)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        AudioDevicesBase.sCW..(self.centralwidget)
        self.statusbar _ ?W...QStatusBar(AudioDevicesBase)
        self.statusbar.setObjectName("statusbar")
        AudioDevicesBase.setStatusBar(self.statusbar)

        self.retranslateUi(AudioDevicesBase)
        self.tabWidget.setCurrentIndex(0)
        ?C...QMetaObject.connectSlotsByName(AudioDevicesBase)

    ___ retranslateUi  AudioDevicesBase):
        _translate _ ?C...QCoreApplication.translate
        AudioDevicesBase.setWindowTitle(_translate("AudioDevicesBase", "Audio Devices"))
        self.modeLabel.sT..(_translate("AudioDevicesBase", "Mode"))
        self.deviceLabel.sT..(_translate("AudioDevicesBase", "Device"))
        self.modeBox.setItemText(0, _translate("AudioDevicesBase", "Input"))
        self.modeBox.setItemText(1, _translate("AudioDevicesBase", "Output"))
        self.actualLabel.sT..(_translate("AudioDevicesBase", "<i>Actual Settings</i>"))
        self.nearestLabel.sT..(_translate("AudioDevicesBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Nearest Settings</span></p></body></html>"))
        self.testButton.sT..(_translate("AudioDevicesBase", "Test"))
        self.actualFreqLabel.sT..(_translate("AudioDevicesBase", "Frequency (Hz)"))
        self.actualChannelLabel.sT..(_translate("AudioDevicesBase", "Channels"))
        self.actualSampleSizeLabel.sT..(_translate("AudioDevicesBase", "Sample size (bits)"))
        self.actualEndianLabel.sT..(_translate("AudioDevicesBase", "Endianess"))
        self.label.sT..(_translate("AudioDevicesBase", "Note: an invalid codec \'audio/test\' exists in order to allow an invalid format to be constructed, and therefore to trigger a \'nearest format\' calculation."))
        self.actualCodecLabel.sT..(_translate("AudioDevicesBase", "Codec"))
        self.actualSampleTypeLabel.sT..(_translate("AudioDevicesBase", "SampleType"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.testFormatTab), _translate("AudioDevicesBase", "Test format"))
        self.populateTableButton.sT..(_translate("AudioDevicesBase", "Populate table"))
        self.allFormatsTable.setSortingEnabled F..
        item _ self.allFormatsTable.horizontalHeaderItem(0)
        item.sT..(_translate("AudioDevicesBase", "Codec"))
        item _ self.allFormatsTable.horizontalHeaderItem(1)
        item.sT..(_translate("AudioDevicesBase", "Frequency (Hz)"))
        item _ self.allFormatsTable.horizontalHeaderItem(2)
        item.sT..(_translate("AudioDevicesBase", "Channels"))
        item _ self.allFormatsTable.horizontalHeaderItem(3)
        item.sT..(_translate("AudioDevicesBase", "Sample type"))
        item _ self.allFormatsTable.horizontalHeaderItem(4)
        item.sT..(_translate("AudioDevicesBase", "Sample size (bits)"))
        item _ self.allFormatsTable.horizontalHeaderItem(5)
        item.sT..(_translate("AudioDevicesBase", "Endianness"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AudioDevicesBase", "All formats"))

