# f2.py 내용
'''
    라우트 추가 -> URL 추가
'''
from flask import Flask,render_template,jsonify,redirect,url_for

app = Flask(__name__)



# 기획서를 기반해서 총 페이지 수 만큼 URL준비
# 뼈대를 먼저 잡아서 각 페이지에 해당하는 URL준비
# blueprint를 사용한다면 대분류,중분류(생략가능),소분류등 틀리 구조로 배치
# /login <-> blueprint 활용: /auth/users/login

@app.route('/')
def home():
    return 'hello world'


# 아래와 같은 url 구성은 blueprint를 사용하여 섹션을 나눠서 관리하는 것이 더 났다 

@app.route('/login')
def login():
    return 'login page'

@app.route('/sign up')
def signup():
    return 'sign up page'


if __name__ == '__main__':
    app.run(debug=True)