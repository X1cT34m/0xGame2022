import random
from flask import Flask, render_template_string, render_template, request
import os
import re


app = Flask(__name__)
#app.config['SECRET_KEY'] = '4hfj8shrt&%^jf*dw'
#app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            p = request.values.get('formula')
            if p != None:
                if re.match("\d{1,10}.?\d{0,5}[\+\-\*\/]\d{1,10}.?\d{0,5}",p):
                    result=eval(p)
                    return render_template_string(str(result))
                if '{{' in p or '}}' in p or 'class' in p or 'import' in p or 'open' in p or 'request' in p or '+' in p or 'lipsum' in p:
                    return 'what\'s this?'
                return render_template_string(p)

        except Exception as e:
            print(e)
            return 'too hard for meQ_Q'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
