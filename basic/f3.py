'''
    클라이언트가 서버에게 데이터를 보내는 방법 
        - 방법 method:GET,POST.,PUT...
            < - 
'''
from flask import Flask,render_template,jsonify,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)
