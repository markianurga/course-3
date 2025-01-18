import sqlite3
from pprint import pprint

conn = sqlite3.connect("m6/u3/Artistc.db")
cursor = conn.cursor()

query = "select * from artists"
cursor.execute(query)
data = cursor.fetchall()
print(len(data))
pprint(data[459])


query = "select * from artists where Gender = 'Female'"
cursor.execute(query)
data = cursor.fetchall()
print(len(data))
pprint(data)

query = "select Name,Gender from artists where Gender = 'Male'"
cursor.execute(query)
data = cursor.fetchall()
print(len(data))
pprint(data)

