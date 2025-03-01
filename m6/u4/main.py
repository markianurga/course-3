from flask import Flask, request, session , render_template ,redirect, url_for
from db import *
import os

folder = os.getcwd()
folder_templates = os.path.join(folder,"m6\\u4\\templates")

app = Flask(__file__, template_folder = folder_templates)
app.config["SECRET_KEY"] = "sessio"


def startquiz(quiz_id):
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session["rezTrue"] = 0  
    session["total"] = 0



def index():
    if request.method == 'GET':
        startquiz(0)
        quizes = getquiz()
        return render_template("index.html", quize = quizes)
    
    if request.method == 'POST':
        q = request.form.get('quiz')
        startquiz(q)
        return redirect(url_for('test'))
    

        

def questionForm(Question):
    QuestionId = Question[0]
    QuestionName = Question[1]
    Answers = Question[2:]


    return render_template("test.html", id=QuestionId, name = QuestionName, ans = Answers)


def test():
    if int(session.get("quiz", 0)) <= 0:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        save_answers()

    Question = getQuestion(session['last_question'], session['quiz'])

    if Question == None or len(Question) == 0:
        return redirect(url_for("result"))
    
    return questionForm(Question)

def save_answers():
    ques_id = request.form.get("q_id")
    a_text = request.form.get("ans_text")
    session['last_question'] = ques_id                
    if checkAnswer(question_id=ques_id,answer_text=a_text) ==  True:
        session["rezTrue"] += 1             
    session["total"] += 1      
    
    
def result():
    return render_template("result.html", tota = session ['total'],rez = session ['rezTrue'])

app.add_url_rule("/", "index", index,methods = ['GET','POST'])
app.add_url_rule("/test", "test", test,methods = ['GET','POST'])
app.add_url_rule("/result", "result", result)

app.run(debug = True)
