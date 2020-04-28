#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ smtpd
______ a..
______ a_p..

c_ CustomSMTPServer(smtpd.SMTPServer):
    
    ___ process_message peer, mailfrom, rcpttos, data):
        print ('Message Received from:', peer)
        print ('From:', mailfrom)
        print ('To  :', rcpttos)
        print ('Message :', data)
        r_

__ _______ __ ______
    parser _ ?.AP..(d.._'Mail Server Example')
    ?.a_a..('--host', a.._"store", d.._"host", type_str, r.._T..)
    ?.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ ?.parse_args()
    server _ CustomSMTPServer((?.host, ?.port), N..)
    ?.loop()

