#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


____ ?.?C.. ______ QFileInfo, QRegExp, ?S.., __
____ ?.?G.. ______ QIcon, QImage, ?P.., ?P..
____ ?.?W.. ______ (QAbstractItemView, ?A.., QActionGroup,
        ?A.., ?CB, ?FD.., QFrame, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QItemDelegate, QLabel, ?MW..,
        ?MB.., QRadioButton, QSizePolicy, SB.., QStyle,
        ?SF.., QTableWidget, QTableWidgetItem, QVBoxLayout, ?W..)


c_ IconSizeSpinBox(SB..):
    @staticmethod
    ___ valueFromText(t__):
        regExp _ QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")

        __ regExp.exactMatch(t__):
            r_ int(regExp.cap(1))
        ____
            r_ 0

    @staticmethod
    ___ textFromValue(value):
        r_ "%d x %d" % (value, value)


c_ ImageDelegate(QItemDelegate):
    ___ createEditor  parent, option, index):
        comboBox _ ?CB(parent)
        __ index.column() __ 1:
            comboBox.aI..("Normal")
            comboBox.aI..("Active")
            comboBox.aI..("Disabled")
            comboBox.aI..("Selected")
        ____ index.column() __ 2:
            comboBox.aI..("Off")
            comboBox.aI..("On")

        comboBox.activated.c..(e..CommitData)

        r_ comboBox

    ___ setEditorData  editor, index):
        comboBox _ editor
        __ no. comboBox:
            r_

        pos _ comboBox.findText(index.model().data(index), __.MatchExactly)
        comboBox.setCurrentIndex(pos)

    ___ setModelData  editor, model, index):
        comboBox _ editor
        __ no. comboBox:
            r_

        model.setData(index, comboBox.currentText())

    ___ e..CommitData
        commitData.e..(sender())


c_ IconPreviewArea(?W..):
    ___  -   parent_None):
        super(IconPreviewArea, self). - (parent)

        mainLayout _ QGridLayout()
        sL..(mainLayout)

        icon _ QIcon()
        size _ ?S..()
        stateLabels _   # list
        modeLabels _   # list
        pixmapLabels _   # list

        stateLabels.ap..(createHeaderLabel("Off"))
        stateLabels.ap..(createHeaderLabel("On"))

        modeLabels.ap..(createHeaderLabel("Normal"))
        modeLabels.ap..(createHeaderLabel("Active"))
        modeLabels.ap..(createHeaderLabel("Disabled"))
        modeLabels.ap..(createHeaderLabel("Selected"))

        ___ j, label __ en..(stateLabels):
            mainLayout.aW..(label, j + 1, 0)

        ___ i, label __ en..(modeLabels):
            mainLayout.aW..(label, 0, i + 1)

            pixmapLabels.ap..(  # list)
            ___ j __ ra..(le.(stateLabels)):
                pixmapLabels[i].ap..(createPixmapLabel())
                mainLayout.aW..(pixmapLabels[i][j], j + 1, i + 1)

    ___ setIcon  icon):
        icon _ icon
        updatePixmapLabels()

    ___ setSize  size):
        __ size !_ size:
            size _ size
            updatePixmapLabels()

    ___ createHeaderLabel  t__):
        label _ QLabel("<b>%s</b>" % t__)
        label.setAlignment(__.AlignCenter)
        r_ label

    ___ createPixmapLabel 
        label _ QLabel()
        label.sE.. F..
        label.setAlignment(__.AlignCenter)
        label.setFrameShape(QFrame.Box)
        label.sSP..(QSizePolicy.E.., QSizePolicy.E..)
        label.setBackgroundRole(?P...Base)
        label.setAutoFillBackground( st.
        label.sMS..(132, 132)
        r_ label

    ___ updatePixmapLabels 
        ___ i __ ra..(le.(modeLabels)):
            __ i __ 0:
                mode _ QIcon.Normal
            ____ i __ 1:
                mode _ QIcon.Active
            ____ i __ 2:
                mode _ QIcon.Disabled
            ____
                mode _ QIcon.Selected

            ___ j __ ra..(le.(stateLabels)):
                state _ QIcon.Off __ j __ 0 ____ QIcon.On
                pixmap _ icon.pixmap(size, mode, state)
                pixmapLabels[i][j].setPixmap(pixmap)
                pixmapLabels[i][j].sE..(no. pixmap.isNull())


c_ MainWindow ?MW..
    ___  -   parent_None):
        super(MainWindow, self). - (parent)

        centralWidget _ ?W..
        sCW..(centralWidget)

        createPreviewGroupBox()
        createImagesGroupBox()
        createIconSizeGroupBox()

        createActions()
        createMenus()
        createContextMenu()

        mainLayout _ QGridLayout()
        mainLayout.aW..(previewGroupBox, 0, 0, 1, 2)
        mainLayout.aW..(imagesGroupBox, 1, 0)
        mainLayout.aW..(iconSizeGroupBox, 1, 1)
        centralWidget.sL..(mainLayout)

        sWT..("Icons")
        checkCurrentStyle()
        otherRadioButton.click()

        r..(minimumSizeHint())

    ___ about 
        ?MB...about  "About Icons",
                "The <b>Icons</b> example illustrates how Qt renders an icon "
                "in different modes (active, normal, disabled and selected) "
                "and states (on and off) based on a set of images.")

    ___ changeStyle  checked):
        __ no. checked:
            r_

        action _ sender()
        style _ ?SF...create(action.data())
        __ no. style:
            r_

        ?A...sS..(style)

        setButtonText(smallRadioButton, "Small (%d x %d)",
                style, QStyle.PM_SmallIconSize)
        setButtonText(largeRadioButton, "Large (%d x %d)",
                style, QStyle.PM_LargeIconSize)
        setButtonText(toolBarRadioButton, "Toolbars (%d x %d)",
                style, QStyle.PM_ToolBarIconSize)
        setButtonText(listViewRadioButton, "List views (%d x %d)",
                style, QStyle.PM_ListViewIconSize)
        setButtonText(iconViewRadioButton, "Icon views (%d x %d)",
                style, QStyle.PM_IconViewIconSize)
        setButtonText(tabBarRadioButton, "Tab bars (%d x %d)",
                style, QStyle.PM_TabBarIconSize)

        changeSize()

    @staticmethod
    ___ setButtonText(button, label, style, metric):
        metric_value _ style.pixelMetric(metric)
        button.sT..(label % (metric_value, metric_value))

    ___ changeSize  checked_ st.:
        __ no. checked:
            r_

        __ otherRadioButton.isChecked
            extent _ otherSpinBox.value()
        ____
            __ smallRadioButton.isChecked
                metric _ QStyle.PM_SmallIconSize
            ____ largeRadioButton.isChecked
                metric _ QStyle.PM_LargeIconSize
            ____ toolBarRadioButton.isChecked
                metric _ QStyle.PM_ToolBarIconSize
            ____ listViewRadioButton.isChecked
                metric _ QStyle.PM_ListViewIconSize
            ____ iconViewRadioButton.isChecked
                metric _ QStyle.PM_IconViewIconSize
            ____
                metric _ QStyle.PM_TabBarIconSize

            extent _ ?A...style().pixelMetric(metric)

        previewArea.setSize(?S..(extent, extent))
        otherSpinBox.sE..(otherRadioButton.isChecked())

    ___ changeIcon 
        icon _ QIcon()

        ___ row __ ra..(imagesTable.rowCount()):
            item0 _ imagesTable.item(row, 0)
            item1 _ imagesTable.item(row, 1)
            item2 _ imagesTable.item(row, 2)

            __ item0.checkState() __ __.Checked:
                __ item1.t__() __ "Normal":
                    mode _ QIcon.Normal
                ____ item1.t__() __ "Active":
                    mode _ QIcon.Active
                ____ item1.t__() __ "Disabled":
                    mode _ QIcon.Disabled
                ____
                    mode _ QIcon.Selected

                __ item2.t__() __ "On":
                    state _ QIcon.On
                ____
                    state _ QIcon.Off

                fileName _ item0.data(__.UserRole)
                image _ QImage(fileName)
                __ no. image.isNull
                    icon.addPixmap(?P...fromImage(image), mode, state)

        previewArea.setIcon(icon)

    ___ addImage 
        fileNames, _ _ ?FD...getOpenFileNames  "Open Images", '',
                "Images (*.png *.xpm *.jpg);;All Files (*)")

        ___ fileName __ fileNames:
            row _ imagesTable.rowCount()
            imagesTable.setRowCount(row + 1)

            imageName _ QFileInfo(fileName).baseName()
            item0 _ QTableWidgetItem(imageName)
            item0.setData(__.UserRole, fileName)
            item0.setFlags(item0.flags() & ~__.IIE..)

            item1 _ QTableWidgetItem("Normal")
            item2 _ QTableWidgetItem("Off")

            __ guessModeStateAct.isChecked
                __ '_act' __ fileName:
                    item1.sT..("Active")
                ____ '_dis' __ fileName:
                    item1.sT..("Disabled")
                ____ '_sel' __ fileName:
                    item1.sT..("Selected")

                __ '_on' __ fileName:
                    item2.sT..("On")

            imagesTable.setItem(row, 0, item0)
            imagesTable.setItem(row, 1, item1)
            imagesTable.setItem(row, 2, item2)
            imagesTable.openPersistentEditor(item1)
            imagesTable.openPersistentEditor(item2)

            item0.setCheckState(__.Checked)

    ___ removeAllImages 
        imagesTable.setRowCount(0)
        changeIcon()

    ___ createPreviewGroupBox 
        previewGroupBox _ QGroupBox("Preview")

        previewArea _ IconPreviewArea()

        layout _ ?VBL..
        layout.aW..(previewArea)
        previewGroupBox.sL..(layout)

    ___ createImagesGroupBox 
        imagesGroupBox _ QGroupBox("Images")

        imagesTable _ QTableWidget()
        imagesTable.setSelectionMode(QAbstractItemView.NoSelection)
        imagesTable.setItemDelegate(ImageDelegate(self))

        imagesTable.horizontalHeader().setDefaultSectionSize(90)
        imagesTable.setColumnCount(3)
        imagesTable.setHorizontalHeaderLabels(("Image", "Mode", "State"))
        imagesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        imagesTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        imagesTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        imagesTable.verticalHeader().hide()

        imagesTable.itemChanged.c..(changeIcon)

        layout _ ?VBL..
        layout.aW..(imagesTable)
        imagesGroupBox.sL..(layout)

    ___ createIconSizeGroupBox 
        iconSizeGroupBox _ QGroupBox("Icon Size")

        smallRadioButton _ QRadioButton()
        largeRadioButton _ QRadioButton()
        toolBarRadioButton _ QRadioButton()
        listViewRadioButton _ QRadioButton()
        iconViewRadioButton _ QRadioButton()
        tabBarRadioButton _ QRadioButton()
        otherRadioButton _ QRadioButton("Other:")

        otherSpinBox _ IconSizeSpinBox()
        otherSpinBox.setRange(8, 128)
        otherSpinBox.setValue(64)

        smallRadioButton.t__.c..(changeSize)
        largeRadioButton.t__.c..(changeSize)
        toolBarRadioButton.t__.c..(changeSize)
        listViewRadioButton.t__.c..(changeSize)
        iconViewRadioButton.t__.c..(changeSize)
        tabBarRadioButton.t__.c..(changeSize)
        otherRadioButton.t__.c..(changeSize)
        otherSpinBox.valueChanged.c..(changeSize)

        otherSizeLayout _ QHBoxLayout()
        otherSizeLayout.aW..(otherRadioButton)
        otherSizeLayout.aW..(otherSpinBox)
        otherSizeLayout.addStretch()

        layout _ QGridLayout()
        layout.aW..(smallRadioButton, 0, 0)
        layout.aW..(largeRadioButton, 1, 0)
        layout.aW..(toolBarRadioButton, 2, 0)
        layout.aW..(listViewRadioButton, 0, 1)
        layout.aW..(iconViewRadioButton, 1, 1)
        layout.aW..(tabBarRadioButton, 2, 1)
        layout.aL..(otherSizeLayout, 3, 0, 1, 2)
        layout.setRowStretch(4, 1)
        iconSizeGroupBox.sL..(layout)

    ___ createActions 
        addImagesAct _ ?A..("&Add Images...", self, shortcut_"Ctrl+A",
                triggered_self.addImage)

        removeAllImagesAct _ ?A..("&Remove All Images", self,
                shortcut_"Ctrl+R", triggered_self.removeAllImages)

        exitAct _ ?A..("&Quit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        styleActionGroup _ QActionGroup
        ___ styleName __ ?SF...keys
            action _ ?A..(styleActionGroup,
                    text_"%s Style" % styleName, checkable_True,
                    triggered_self.changeStyle)
            action.setData(styleName)

        guessModeStateAct _ ?A..("&Guess Image Mode/State", self,
                checkable_True, checked_ st.

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus 
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(addImagesAct)
        fileMenu.aA..(removeAllImagesAct)
        fileMenu.addSeparator()
        fileMenu.aA..(exitAct)

        viewMenu _ mB.. .aM..("&View")
        ___ action __ styleActionGroup.actions
            viewMenu.aA..(action)
        viewMenu.addSeparator()
        viewMenu.aA..(guessModeStateAct)

        mB.. .addSeparator()

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ createContextMenu 
        imagesTable.setContextMenuPolicy(__.ActionsContextMenu)
        imagesTable.aA..(addImagesAct)
        imagesTable.aA..(removeAllImagesAct)

    ___ checkCurrentStyle 
        ___ action __ styleActionGroup.actions
            styleName _ action.data()
            candidate _ ?SF...create(styleName)

            __ candidate __ N..:
                r_

            __ candidate.metaObject().className() __ ?A...style().metaObject().className
                action.trigger()


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e..(app.exec_())
