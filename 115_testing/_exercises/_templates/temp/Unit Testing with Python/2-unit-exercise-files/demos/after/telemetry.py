DiagnosticChannelConnectionString _ "*111#"

c_ TelemetryDiagnosticControls:

    ___  -   telemetry_client_N..
        telemetry_client _ telemetry_client o. TelemetryClient()
        diagnostic_info _ ""

    ___ check_transmission
        telemetry_client _ reconnect(DiagnosticChannelConnectionString)
        diagnostic_info _ ""
        diagnostic_info _ fetch_diagnostic_info(telemetry_client)

    ___ reconnect  address
        telemetry_client.disconnect()
        retryLeft _ 3
        while ((no. telemetry_client.online_status) and retryLeft > 0
            telemetry_client.connect(address)
            retryLeft -_ 1

        __ no. telemetry_client.online_status:
            r_ Exception("Unable to connect.")
        r_ telemetry_client

    ___ fetch_diagnostic_info  connected_client
        connected_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        __ no. telemetry_client.online_status:
            r_ Exception("Unable to connect.")
        r_ connected_client.receive()



c_ TelemetryClient(object
    DIAGNOSTIC_MESSAGE _ "AT#UD"

    ___  -
        online_status _ F..
        _diagnostic_message_result _ ""

    ___ connect  telemetry_server_connection_string
        __ no. telemetry_server_connection_string:
            r_ Exception()

        # simulate the operation on a real modem
        success _ ra__.randint(0, 10) <_ 8
        online_status _ success

    ___ disconnect
        online_status _ F..

    ___ send  message
        __ no. message:
            r_ Exception()

        __ message __ TelemetryClient.DIAGNOSTIC_MESSAGE:
            # simulate a status report
            _diagnostic_message_result _ """\
LAST TX rate................ 100 MBPS\r\n
HIGHEST TX rate............. 100 MBPS\r\n
LAST RX rate................ 100 MBPS\r\n
HIGHEST RX rate............. 100 MBPS\r\n
BIT RATE.................... 100000000\r\n
WORD LEN.................... 16\r\n
WORD/FRAME.................. 511\r\n
BITS/FRAME.................. 8192\r\n
MODULATION TYPE............. PCM/FM\r\n
TX Digital Los.............. 0.75\r\n
RX Digital Los.............. 0.10\r\n
BEP Test.................... -5\r\n
Local Rtrn Count............ 00\r\n
Remote Rtrn Count........... 00"""

            r_
        # here should go the real Send operation (not needed for this exercise)

    ___ receive
        __ no. _diagnostic_message_result:
            # simulate a received message (just for illustration - not needed for this exercise)
            message _ ""
            messageLength _ ra__.randint(0, 50) + 60
            i _ messageLength
            while(i >_ 0
                message +_ chr((ra__.randint(0, 40) + 86))
                i -_ 1
        else:
            message _ _diagnostic_message_result
            _diagnostic_message_result _ ""

        r_ message
