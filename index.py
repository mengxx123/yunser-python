# -*- coding:utf-8 -*-
# print("Hello, World!");

import json
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, request, Response, jsonify
import uuid

app = Flask(__name__)
# app.run(host='0.0.0.0')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/about')
def about():
    return 'Yunser 1.0.3'



@app.route('/emotion')
def emotion():
    thetext = request.args.get('text')
    templateId = request.args.get('templateId')
    y = int(request.args.get('y'))
    img = Image.open('./template/template-' + templateId + '.jpg')
    font = ImageFont.truetype('./yahei.ttf', 22)
    imgWidth, imgHeight = img.size
    text = thetext # .decode('utf-8')
    draw = ImageDraw.Draw(img)
    fontWidth, fontHeight = draw.textsize(text, font)
    draw.text(((imgWidth - fontWidth) / 2, y), text, (0, 0, 0), font, align="center")    #设置文字位置/内容/颜色/字体
    draw = ImageDraw.Draw(img)                          #Just draw it!
    #另存图片
    print('123')
    fileName = str(uuid.uuid1())
    print(fileName)
    img.save('./static/' + fileName + '.jpg')
    return '/static/' + fileName + '.jpg'

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
    return "Hello World!2021"

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
