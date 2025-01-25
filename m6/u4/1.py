import sqlite3
from pprint import pprint

conn = sqlite3.connect("m6/u4/Quiz.db")
cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS quiz  (
        id INTEGER,
        name VARCHAR)
"""
cursor.execute(query)
conn.commit()
 
query = """
    CREATE TABLE IF NOT EXISTS  question  (
        id INTEGER,
        Question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR
    )
"""
cursor.execute(query)
conn.commit()
 