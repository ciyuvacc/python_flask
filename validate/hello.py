#coding:utf-8
from flask import Flask
from flask import render_template
from models import *
from flask import request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/validate/',methods = ['post','get'])
def validate():
    if request.method == 'GET':
        name = request.args.get('username')
        password = request.args.get('password')
    else:
        name = request.form.get('username')
        password = request.form.get('password')
    if name=='ws' and password == '1234': 
        return redirect('/logs/')
    else:
        return render_template('login.html',err='login fail')

@app.route('/logs/')
def logstatus():
    logls=logs.logs()
    return render_template('logs.html',logls=logls)


if __name__== '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
