______  ?

sock = ?.?(?.A_I.., ?.S_S..)
?.b..(('127.0.0.1', 8888))
?.l..(5)
# sock.setblocking(True)
# sock.settimeout(5)
# sock.settimeout(0)  # ->  sock.blocking(False)
?.settimeout(None)  # ->  sock.blocking(True)

___
    client, addr = ?.a..
_____ ?.error:
    print('No connections')
# except socket.timeout:
#     print('timed out')
____
    result = client.r..(1024)
    client.c..
    print('Message', result.d..('utf-8'))
