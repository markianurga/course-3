from flask import Flask

app = Flask(__file__)



def index():
    return "hi"
def test():
    return "neme"
    
    
def result():
    return "fer"

app.add_url_rule("/", "index", index)
app.add_url_rule("/test", "test", test)
app.add_url_rule("/result", "result", result)

app.run()
