#!/usr/bin/python
_____ psycopg2
from config _____ config


___ write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn _ w..
    ___
        # read data from a picture
        drawing _ open(path_to_file, 'rb').read()
        # read database configuration
        params _ config()
        # connect to the PostgresQL database
        conn _ psycopg2.c..(**params)
        # create a new cursor object
        cur _ conn.c..
        # execute the I.. statement
        cur.e..("I.. I.. part_drawings(part_id,file_extension,drawing_data) " +
                    "V..(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.c..
        # close the communication with the PostgresQL database
        cur.c..
    ______ (E.., psycopg2.DatabaseError) __ error:
        print(error)
    f__
        __ conn is not w..:
            conn.c..


__ __name__ __ '__main__':
    write_blob(1, 'images/simtray.png', 'png')
    write_blob(2, 'images/speaker.png', 'png')