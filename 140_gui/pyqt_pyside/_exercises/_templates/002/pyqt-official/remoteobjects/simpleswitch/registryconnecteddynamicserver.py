#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2018 Riverbank Computing Limited
## Copyright (C) 2017 Ford Motor Company
##
## This file is part of the PyQt examples.
##
## $QT_BEGIN_LICENSE:BSD$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## BSD License Usage
## Alternatively, you may use this file under the terms of the BSD license
## as follows:
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
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
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


______ ___

____ ?.?C.. ______ (pP.., pS.., pyqtSlot,  ?CA..,
        ?O.., ?T.., ?U..)
____ ?.QtRemoteObjects ______ QRemoteObjectHost, QRemoteObjectRegistryHost


c_ SimpleSwitch(?O..):

    ___  -   parent_None):
        s_. - (parent)

        _currState _ F..

        _stateChangeTimer _ ?T..
        _stateChangeTimer.timeout.c..(_timeout)
        _stateChangeTimer.start(2000)

        print("Source node started")

    # PyQt does not support the use of static source types defined in .rep
    # files.  However we can manually specify a dynamic type that matches a
    # .rep defined type by defining properties, signals and slots in the same
    # order.  We also have to account for any internals also generated by the
    # .rep generator.  At the moment this only includes an extra 'push' slot
    # for each property (that never seems to get called).  This allows this
    # example to act as a server for Qt's C++ 'directconnectclient' example.
    # It is not necessary when using with clients that use dynamic source types
    # (written using either C++ or Python).
    @pyqtSlot()
    ___ pushCurrState  currState):
        p..

    ___ _get_currState 
        r_ _currState

    ___ _set_currState  value):
        # If the value has changed then update it and emit the notify signal.
        __ _currState !_ value:
            _currState _ value
            currStateChanged.e..(value)

    # The property's notify signal.
    currStateChanged _ pS..(bool)

    # The property exposed to a remote client.
    currState _ pP..(bool, fget__get_currState, fset__set_currState,
            notify_currStateChanged)

    # The slot exposed to a remote client.
    @pyqtSlot(bool)
    ___ server_slot  clientState):
        # The switch state echoed back by the client.
        print("Replica state is", clientState)

    ___ _timeout 
        # Note that we don't decorate this callable so that it doesn't get
        # exposed in a replica.
        currState _ no. currState

        print("Source state is", currState)


__ ______ __ ______

    app _  ?CA..(___.a..

    # Create the simple switch.
    srcSwitch _ SimpleSwitch()

    # Create the node that hosts the registry.  This could be in a separate
    # process.
    regNode _ QRemoteObjectRegistryHost(?U..('local:registry'))

    # Create the host object node.  This will connect to the registry node
    # rather than to a client.
    srcNode _ QRemoteObjectHost(?U..('local:replica'), ?U..('local:registry'))

    # Enable remoting.
    srcNode.enableRemoting(srcSwitch, 'SimpleSwitch')

    ___.e.. ?.e..
