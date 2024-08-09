from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
     return render_template('Index.html')

@app.route("/viewdata",methods=['GET', 'POST'])
def hello1():
    if request.method=='GET':
        fullname=request.args.get('fname')
        age=request.args.get('age')
        return render_template('page2.html',fullname=fullname,age=int(age))
