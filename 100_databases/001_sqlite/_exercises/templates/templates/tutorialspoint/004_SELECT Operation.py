#!/usr/bin/python

_____ ?

conn _ ?.c..(d.. _ "testdb", u.. _ "postgres", p.. _ "pass123", h.. _ "127.0.0.1", p.. _ "5432")
print("Opened database successfully")

cur _ conn.c..

cur.e..("S.. id, name, address, salary  f.. COMPANY")
rows _ cur.f_a..
___ row __ rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.c..



# Opened database successfully
# ID =  1
# NAME =  Paul
# ADDRESS =  California
# SALARY =  20000.0
#
# ID =  2
# NAME =  Allen
# ADDRESS =  Texas
# SALARY =  15000.0
#
# ID =  3
# NAME =  Teddy
# ADDRESS =  Norway
# SALARY =  20000.0
#
# ID =  4
# NAME =  Mark
# ADDRESS =  Rich-Mond
# SALARY =  65000.0
#
# Operation done successfully