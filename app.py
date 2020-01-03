import os
from flask import Flask
from flask import request
from flask import render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/', methods=['POST'])
def my_form_post():
    usn = request.form['text']
    usn_file=open('usn.csv','r')
    for info in usn_file:
        info=info.strip('\n')
        info=info.split(',')
        if info[0]==usn:
            return (redirect(url_for('vote')))

        
@app.route('/vote')
def vote():
    return render_template("vote.html")

@app.route('/vote', methods=['POST'])
def voting_form1():
    if "button1" in request.form:
        return ("You voted for 1")
    elif "button2" in request.form:
        return ("You voted for 2")

if __name__ == '__main__':
    app.run()
