# 사용자가 정의한(커스텀) 엔트리 포인트
from flask import Flask,render_template,jsonify,redirect,url_for,request

def create_app():
    app = Flask(__name__)
    init_blueprint(app)

    return app

def init_blueprint(app):
    # app에 블루프린트 객체를 등록한다

    # 실습 http://127.0.0.1:5000/auth접속시 인증홈이란 내용이 나오도록
    # auth관련 블루 프린트를 구성하시오
    from .controllers import main_controller
    from .controllers import auth_controller

    # 이 위치에서는 service를 생략하고 표현가능
    # from service.controller import bp_main
    from .controllers import bp_main,bp_auth

    # 플라스크 객체에 블루 프린트접속
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)

    pass