# -*- coding:utf-8 -*-
# print("Hello, World!");

import json
from flask import Flask
app = Flask(__name__)
# app.run(host='0.0.0.0')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'Yunser 1.0!'

@app.route('/json')
def jsonC():
    t = {
        'name': '张三',
        'age': 24,
        'list': ['1', '2', '3']
    }
    # t.asd = 'asd'
    # t['data'] = s
    return json.dumps(t, ensure_ascii=False)

if __name__ == '__main__':
    app.run()