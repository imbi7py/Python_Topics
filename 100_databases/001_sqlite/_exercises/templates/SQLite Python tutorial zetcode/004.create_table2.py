_____ ? __ ?

cars _ (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

con _ ?.c..('ydb.db')

w__ con:

    cur _ con.c..

    cur.e..("DROP T.. IF EXISTS cars")
    cur.e..("C.. T.. cars(id IN., name T..., price IN.)")
    cur.e_m_("I.. I.. cars V..(?, ?, ?)", cars)