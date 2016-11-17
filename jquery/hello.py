#coding:utf-8
from flask import Flask
from flask import render_template
from flask import request,redirect
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')



if __name__== '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
