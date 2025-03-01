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
    
def close():
    conn.commit()
    cursor.close()
    conn.close()



def CREATE_TABLE():
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
    close()


def add_question():
    open()
    list_q = [('Скільки місяців на рік мають 28 днів?', 
           'Всі', 'Один', 'Ні одного', 'Два'),
          ('Чому дорівнює число Пі?', 
           'Приблизно 3.14', '3', '0', 'Рівно 3.14'), 
          ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрим', 'Червоним', 'Не зміниться', 'Фіолетовим'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Любою'),
        ('Що не має довжини, глибини, ширини, висоти, а можна виміряти?', 'Час', 'Дурність', 'Море', 'Повітря')]

    cursor.executemany('''INSERT INTO question 
                 (question, answer, wrong1, wrong2, wrong3) 
                  VALUES (?,?,?,?,?)''', list_q)
    close()
    
def add_quiz():
    open()
    list_q = [
        ('Початковий квіз',),
        ('Середній квіз',),
        ('Хард квіз',)
    ]

    cursor.executemany('''INSERT INTO  quiz
                 (name) 
                  VALUES (?)''', list_q)
    close()

def getquiz():
    open()
    
    quize = "SELECT * FROM quiz"
    do (quize)
    rez = cursor.fetchall()
    close()
    return rez
    
def getQuestion(question_id, quiz_id):
    open()
    query = ''' 
    SELECT quiz_content.id, question.Question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? 
    AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id
    '''
    cursor.execute(query,[question_id, quiz_id])
    rezalt = cursor.fetchone()
    close()
    return rezalt

def checkAnswer(question_id, answer_text):
    open()
    query =  '''
        SELECT answer FROM question
        WHERE id == ?
    '''
    
    cursor.execute(query,[question_id])
    
    allQues = cursor.fetchone()
    close()
    
    if allQues[0] == answer_text:
        return True
    else:
        return False



    


 
if __name__ == "__main__":
    CREATE_TABLE()
    add_question()
    add_quiz()