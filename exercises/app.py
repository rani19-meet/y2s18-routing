from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/hello')
def home():
    #return render_template(
    #'student.html', student_id = 4)
    return render_template(
    'hello.html')
app.run(debug=True)
