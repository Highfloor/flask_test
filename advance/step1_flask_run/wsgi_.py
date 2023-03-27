from flask import Flask,render_template,jsonify,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page wsgi'
