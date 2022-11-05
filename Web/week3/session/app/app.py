import random
from flask import Flask, render_template_string, render_template, request,session
import os
import re
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = '4hf3j8sgh(rt&%^jf*dw'
#app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    session['user']='nobody'
    session['id']='flag in /admin'
    if request.method == 'POST':
        try:
            p = request.values.get('formula')
            if p != None:
                if re.match("\d{1,10}.?\d{0,5}[\+\-\*\/]\d{1,10}.?\d{0,5}",p):
                    result=eval(p)
                    return render_template_string(str(result))
                if len(p) > 10:
                    return 'what\'s this?'
                return render_template_string(p)

        except Exception as e:
            print(e)
            return 'too hard for meQ_Q'

    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def check():
    if 'user' in session:
        if session.get('user') == 'admin' and session.get('id') == '0':
            return 'Welcome,admin!This is you flag:'+config.FLAG
    return 'who R you?'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
