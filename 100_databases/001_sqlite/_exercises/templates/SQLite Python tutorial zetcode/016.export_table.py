#!/usr/bin/env python3
# -*- coding: utf-8 -*-

_____ ? __ ?

cars _ (
    (1, 'Audi', 52643),
    (2, 'Mercedes', 57642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


___ writeData(data):

    f _ open('cars.sql', 'w')

    with f:
        f.write(data)


con _ ?.c..(':memory:')

with con:

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS cars")
    cur.e..("C.. T.. cars(id IN., name T..., price IN.)")
    cur.e_m_("I.. I.. cars V..(?, ?, ?)", cars)
    cur.e..("D.. F.. cars WHERE price < 30000")

    data _ '\n'.join(con.iterdump())

    writeData(data)