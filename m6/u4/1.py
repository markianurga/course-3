import sqlite3
from pprint import pprint

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect("m6/u4/Quiz.db")
    cursor = conn.cursor()

def do (query):
    cursor.execute(query)
    conn.commit()
open()
query = """
    CREATE TABLE IF NOT EXISTS quiz  (
        id INTEGER primary key,
        name VARCHAR)
"""

do (query)
 
query = """
    CREATE TABLE IF NOT EXISTS  question  (
        id INTEGER primary key,
        Question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR
    )
"""

do (query)
 
query = """
    CREATE TABLE IF NOT EXISTS  quiz_content (
        id INTEGER primary key,
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id),
        FOREIGN KEY (question_id) REFERENCES question (id)

    )
"""

do (query)

 