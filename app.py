from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return (
        'Fullname: Princess DJ D. Milay <br>'
        'Section: BSIT 3-A 2nd 25 <br>'
        'Subject: System Integration and Architecture 1 <br>'
        'Semi-Final Exam'
    )