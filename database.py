import sqlite3
connection=sqlite3.connect("gfg.db")
crsr=connection.cursor()

print("Connected to database")
connection.close()