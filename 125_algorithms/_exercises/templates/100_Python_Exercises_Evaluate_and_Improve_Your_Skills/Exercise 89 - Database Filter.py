#Please download the database file database.db. The file contains a table with 50 country names along with their area in square km and population.
#Please use Python to print out those countries that have an area of greater than 2,000,000.
______ sqlite3

conn _ sqlite3.connect("database.db")
cur _ conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows _ cur.fetchall()
conn.c..
print(rows)

___ i __ rows:
    print(i[0])
