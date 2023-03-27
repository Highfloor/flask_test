# 사용자가 정의한(커스텀) 엔트리 포인트
from flask import Flask,render_template,jsonify,redirect,url_for,request

def create_app():
    app = Flask(__name__)
    # 환경변수 초기화
    init_enviroment(app)
    # 블루프린트 초기화
    init_blueprint(app)

    return app

def init_enviroment(app):
    # 특정 파일(cfg,...)등을 읽어서 처리 가능
    app.config.from_pyfile('resource/config.cfg',silent=True)
    # py을 모듈가져오기 해서 (객체)를 세팅해서 처리
    import service.config as config
    app.config.from_object(config)
    # 환경변수(OS레벨,플라스크 레벨,사용자 정의 레벨) 모두 출력
    print('\n'+'-'*20)
    # 개별 환경 변수값 추출
    print(app.config['SECRET_KEY'], app.config.get('SECRET_KEY'))
    #for k,v in app.config.items():
    #    print(k,v)
    print('-'*20+'\n')
    pass

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