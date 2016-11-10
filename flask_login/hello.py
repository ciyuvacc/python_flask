from flask import Flask,render_template,url_for,request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import os,sys

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/Deploy_container', methods=['GET', 'POST'])
def deploy():
    if request.method == "POST": 
         imagename = ''
         cpus = ''
         memory = ''
         imagename = request.form.get('imagename',default='')    
         name = request.form.get('name',default='')    
         value = request.form.get('value',default='')    
         cpus = request.form.get('cpus',default='')    
         memory = request.form.get('memory',default='')    
         print imagename,name,value,cpus,memory 
         cmd_run = 'docker run -d   --cpu-shares   '  + cpus + ' -m  '  +  memory + '  ' + imagename 
         print cmd_run
         result = os.popen(cmd_run).read()
         print result
         return render_template('result.html',result = result)
    else:
         return render_template('Deploy_container.html')
    


if __name__ == '__main__':
    manager.run()
