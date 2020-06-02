#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2017 Riverbank Computing Limited.
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


____ ?.?C.. ______ QModelIndex, __
____ ?.?G.. ______ QStandardItemModel
____ ?.?W.. ______ (?A.., SB.., QStyledItemDelegate,
        QTableView)


c_ SpinBoxDelegate(QStyledItemDelegate):
    ___ createEditor  parent, option, index):
        editor _ SB..(parent)
        editor.setFrame F..
        editor.setMinimum(0)
        editor.setMaximum(100)

        r_ editor

    ___ setEditorData  spinBox, index):
        value _ index.model().data(index, __.ER..)

        spinBox.setValue(value)

    ___ setModelData  spinBox, model, index):
        spinBox.interpretText()
        value _ spinBox.value()

        model.setData(index, value, __.ER..)

    ___ updateEditorGeometry  editor, option, index):
        editor.setGeometry(option.rect)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    model _ QStandardItemModel(4, 2)
    tableView _ ?TV..
    tableView.sM..(model)

    delegate _ SpinBoxDelegate()
    tableView.setItemDelegate(delegate)

    ___ row __ ra..(4):
        ___ column __ ra..(2):
            index _ model.index(row, column, QModelIndex())
            model.setData(index, (row + 1) * (column + 1))

    tableView.sWT..("Spin Box Delegate")
    tableView.s..
    ___.e..(app.exec_())
