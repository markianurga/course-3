from flask import Flask, render_template
from db import getquiz
import os

folder = os.getcwd()
folder_templates = os.path.join(folder,"m6\\u4\\templates")

app = Flask(__file__, template_folder = folder_templates)



def index():
    quizes = getquiz()
    return render_template("index.html", quize = quizes)



def test():
    return "neme"
    
    
def result():
    return "fer"

app.add_url_rule("/", "index", index)
app.add_url_rule("/test", "test", test)
app.add_url_rule("/result", "result", result)

app.run(debug = True)
