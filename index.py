# -*- coding:utf-8 -*-
# print("Hello, World!");

import json
from flask import Flask, request, Response, jsonify
app = Flask(__name__)
# app.run(host='0.0.0.0')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

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

@app.route("/")
def hello():
    return "Hello World!yunser2 09-09"

@app.route('/test')
def test():
    print('finished')
    name = request.args.get('name')
    return jsonify({
        'name': name
    })

@app.route('/post', methods = ['POST'])
def post():
    data = json.loads(request.data)
    print(data)
    return jsonify({
        'name': data['name']
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
