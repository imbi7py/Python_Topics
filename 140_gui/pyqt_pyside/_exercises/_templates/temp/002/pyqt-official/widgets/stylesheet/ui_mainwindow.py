# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 26 06:49:55 2013
#      by: PyQt5 UI code generator 5.0.1-snapshot-2a99e59669ee
#
# WARNING! All changes made in this file will be lost!

____ ? ______ ?C.., ?G.., ?W..

c_ Ui_MainWindow o..
    ___ setupUi  MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(400, 413)
        centralwidget _ ?W...?W..(MainWindow)
        centralwidget.setObjectName("centralwidget")
        vboxlayout _ ?W...?VBL..(centralwidget)
        vboxlayout.sCM..(9, 9, 9, 9)
        vboxlayout.setSpacing(6)
        vboxlayout.setObjectName("vboxlayout")
        mainFrame _ ?W...QFrame(centralwidget)
        mainFrame.setFrameShape(?W...QFrame.StyledPanel)
        mainFrame.setFrameShadow(?W...QFrame.Raised)
        mainFrame.setObjectName("mainFrame")
        gridlayout _ ?W...QGridLayout(mainFrame)
        gridlayout.sCM..(9, 9, 9, 9)
        gridlayout.setSpacing(6)
        gridlayout.setObjectName("gridlayout")
        agreeCheckBox _ ?W...QCheckBox(mainFrame)
        agreeCheckBox.setObjectName("agreeCheckBox")
        gridlayout.aW..(agreeCheckBox, 6, 0, 1, 5)
        label _ ?W...QLabel(mainFrame)
        label.setAlignment(?C...__.AlignRight|?C...__.AlignTop|?C...__.AlignTrailing)
        label.setObjectName("label")
        gridlayout.aW..(label, 5, 0, 1, 1)
        nameLabel _ ?W...QLabel(mainFrame)
        nameLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        nameLabel.setObjectName("nameLabel")
        gridlayout.aW..(nameLabel, 0, 0, 1, 1)
        maleRadioButton _ ?W...QRadioButton(mainFrame)
        maleRadioButton.setObjectName("maleRadioButton")
        gridlayout.aW..(maleRadioButton, 1, 1, 1, 1)
        passwordLabel _ ?W...QLabel(mainFrame)
        passwordLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        passwordLabel.setObjectName("passwordLabel")
        gridlayout.aW..(passwordLabel, 3, 0, 1, 1)
        countryCombo _ ?W...?CB(mainFrame)
        countryCombo.setObjectName("countryCombo")
        countryCombo.aI..("")
        countryCombo.aI..("")
        countryCombo.aI..("")
        countryCombo.aI..("")
        countryCombo.aI..("")
        countryCombo.aI..("")
        countryCombo.aI..("")
        gridlayout.aW..(countryCombo, 4, 1, 1, 4)
        ageLabel _ ?W...QLabel(mainFrame)
        ageLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        ageLabel.setObjectName("ageLabel")
        gridlayout.aW..(ageLabel, 2, 0, 1, 1)
        countryLabel _ ?W...QLabel(mainFrame)
        countryLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        countryLabel.setObjectName("countryLabel")
        gridlayout.aW..(countryLabel, 4, 0, 1, 1)
        genderLabel _ ?W...QLabel(mainFrame)
        genderLabel.setAlignment(?C...__.AlignRight|?C...__.AlignTrailing|?C...__.AlignVCenter)
        genderLabel.setObjectName("genderLabel")
        gridlayout.aW..(genderLabel, 1, 0, 1, 1)
        passwordEdit _ ?W...QLineEdit(mainFrame)
        passwordEdit.setEchoMode(?W...QLineEdit.Password)
        passwordEdit.setObjectName("passwordEdit")
        gridlayout.aW..(passwordEdit, 3, 1, 1, 4)
        femaleRadioButton _ ?W...QRadioButton(mainFrame)
        femaleRadioButton.setObjectName("femaleRadioButton")
        gridlayout.aW..(femaleRadioButton, 1, 2, 1, 2)
        ageSpinBox _ ?W...SB..(mainFrame)
        ageSpinBox.setMinimum(12)
        ageSpinBox.setProperty("value", 22)
        ageSpinBox.setObjectName("ageSpinBox")
        gridlayout.aW..(ageSpinBox, 2, 1, 1, 2)
        nameCombo _ ?W...?CB(mainFrame)
        nameCombo.setEditable( st.
        nameCombo.setObjectName("nameCombo")
        gridlayout.aW..(nameCombo, 0, 1, 1, 4)
        spacerItem _ ?W...?SI..(40, 20, ?W...?SP...E.., ?W...?SP...Minimum)
        gridlayout.aI..(spacerItem, 1, 4, 1, 1)
        spacerItem1 _ ?W...?SI..(61, 20, ?W...?SP...E.., ?W...?SP...Minimum)
        gridlayout.aI..(spacerItem1, 2, 3, 1, 2)
        buttonBox _ ?W...QDialogButtonBox(mainFrame)
        buttonBox.setOrientation(?C...__.H..)
        buttonBox.setStandardButtons(?W...QDialogButtonBox.Cancel|?W...QDialogButtonBox.NoButton|?W...QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridlayout.aW..(buttonBox, 7, 3, 1, 2)
        professionList _ ?W...QListWidget(mainFrame)
        professionList.setObjectName("professionList")
        item _ ?W...QListWidgetItem()
        professionList.aI..(item)
        item _ ?W...QListWidgetItem()
        professionList.aI..(item)
        item _ ?W...QListWidgetItem()
        professionList.aI..(item)
        gridlayout.aW..(professionList, 5, 1, 1, 4)
        vboxlayout.aW..(mainFrame)
        MainWindow.sCW..(centralwidget)
        menubar _ ?W...QMenuBar(MainWindow)
        menubar.setGeometry(?C...QRect(0, 0, 400, 29))
        menubar.setObjectName("menubar")
        menu_File _ ?W...?M..(menubar)
        menu_File.setObjectName("menu_File")
        menu_Help _ ?W...?M..(menubar)
        menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(menubar)
        statusbar _ ?W...QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(statusbar)
        exitAction _ ?W...?A..(MainWindow)
        exitAction.setObjectName("exitAction")
        aboutQtAction _ ?W...?A..(MainWindow)
        aboutQtAction.setObjectName("aboutQtAction")
        editStyleAction _ ?W...?A..(MainWindow)
        editStyleAction.setObjectName("editStyleAction")
        aboutAction _ ?W...?A..(MainWindow)
        aboutAction.setObjectName("aboutAction")
        menu_File.aA..(editStyleAction)
        menu_File.addSeparator()
        menu_File.aA..(exitAction)
        menu_Help.aA..(aboutAction)
        menu_Help.aA..(aboutQtAction)
        menubar.aA..(menu_File.menuAction())
        menubar.aA..(menu_Help.menuAction())
        label.setBuddy(professionList)
        nameLabel.setBuddy(nameCombo)
        passwordLabel.setBuddy(passwordEdit)
        ageLabel.setBuddy(ageSpinBox)
        countryLabel.setBuddy(countryCombo)

        retranslateUi(MainWindow)
        countryCombo.sCI..(6)
        professionList.setCurrentRow(0)
        ?C...QMetaObject.connectSlotsByName(MainWindow)

    ___ retranslateUi  MainWindow):
        _translate _ ?C... ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Style Sheet"))
        agreeCheckBox.sTT..(_translate("MainWindow", "Please read the LICENSE file before checking"))
        agreeCheckBox.sT..(_translate("MainWindow", "I accept the terms and &conditions"))
        label.sT..(_translate("MainWindow", "Profession:"))
        nameLabel.sT..(_translate("MainWindow", "&Name:"))
        maleRadioButton.sTT..(_translate("MainWindow", "Check this if you are male"))
        maleRadioButton.sT..(_translate("MainWindow", "&Male"))
        passwordLabel.sT..(_translate("MainWindow", "&Password:"))
        countryCombo.sTT..(_translate("MainWindow", "Specify country of origin"))
        countryCombo.setStatusTip(_translate("MainWindow", "Specify country of origin"))
        countryCombo.setItemText(0, _translate("MainWindow", "Egypt"))
        countryCombo.setItemText(1, _translate("MainWindow", "France"))
        countryCombo.setItemText(2, _translate("MainWindow", "Germany"))
        countryCombo.setItemText(3, _translate("MainWindow", "India"))
        countryCombo.setItemText(4, _translate("MainWindow", "Italy"))
        countryCombo.setItemText(5, _translate("MainWindow", "Norway"))
        countryCombo.setItemText(6, _translate("MainWindow", "Pakistan"))
        ageLabel.sT..(_translate("MainWindow", "&Age:"))
        countryLabel.sT..(_translate("MainWindow", "Country:"))
        genderLabel.sT..(_translate("MainWindow", "Gender:"))
        passwordEdit.sTT..(_translate("MainWindow", "Specify your password"))
        passwordEdit.setStatusTip(_translate("MainWindow", "Specify your password"))
        passwordEdit.sT..(_translate("MainWindow", "Password"))
        femaleRadioButton.sTT..(_translate("MainWindow", "Check this if you are female"))
        femaleRadioButton.sT..(_translate("MainWindow", "&Female"))
        ageSpinBox.sTT..(_translate("MainWindow", "Specify your age"))
        ageSpinBox.setStatusTip(_translate("MainWindow", "Specify your age"))
        nameCombo.sTT..(_translate("MainWindow", "Specify your name"))
        professionList.sTT..(_translate("MainWindow", "Select your profession"))
        professionList.setStatusTip(_translate("MainWindow", "Specify your name here"))
        professionList.setWhatsThis(_translate("MainWindow", "Specify your name here"))
        __sortingEnabled _ professionList.isSortingEnabled()
        professionList.setSortingEnabled F..
        item _ professionList.item(0)
        item.sT..(_translate("MainWindow", "Developer"))
        item _ professionList.item(1)
        item.sT..(_translate("MainWindow", "Student"))
        item _ professionList.item(2)
        item.sT..(_translate("MainWindow", "Fisherman"))
        professionList.sSE..__sortingEnabled)
        menu_File.setTitle(_translate("MainWindow", "&File"))
        menu_Help.setTitle(_translate("MainWindow", "&Help"))
        exitAction.sT..(_translate("MainWindow", "&Exit"))
        aboutQtAction.sT..(_translate("MainWindow", "About Qt"))
        editStyleAction.sT..(_translate("MainWindow", "Edit &Style..."))
        aboutAction.sT..(_translate("MainWindow", "About"))

