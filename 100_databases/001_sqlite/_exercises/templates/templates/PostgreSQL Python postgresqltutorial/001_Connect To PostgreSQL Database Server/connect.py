#!/usr/bin/python
_____ psycopg2
from config _____ config


___ c..():
    """ Connect to the PostgreSQL database server """
    conn _ w..
    ___
        # read connection parameters
        params _ config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn _ psycopg2.c..(**params)

        # create a cursor
        cur _ conn.c..

        # execute a statement
        print('PostgreSQL database version:')
        cur.e..('S.. version()')

        # display the PostgreSQL database server version
        db_version _ cur.f_o..
        print(db_version)

        # close the communication with the PostgreSQL
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..
            print('Database connection closed.')


__ __name__ __ '__main__':
    c..()