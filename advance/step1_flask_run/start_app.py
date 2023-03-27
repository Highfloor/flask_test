# 사용자가 정의한(커스텀) 엔트리 포인트
from flask import Flask,render_template,jsonify,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page 커스텀'
