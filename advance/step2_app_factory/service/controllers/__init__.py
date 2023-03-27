from flask import Blueprint

# 메인 서비스 페이지 - A 개발자 담당 -> 모든 url은 ~/main/~

bp_main = Blueprint('main_bp', # 별칭, 해당 블루프린트 밑에서 정의된 
                               # 라우트 및 함수를 url_for('main_bp.home')으로 지칭할때 사용
                    __name__,  # 고정
                    url_prefix='/main', # 모든 URL앞에 /main이 추가된다
                    template_folder='../templates/main', # html위치하는 폴더지정
                    static_folder='../static'       # 정적 데이터가 위치하는 폴더
                    )


# 인증 관련 서비스 - B개발자가 담당 -> 모든 URL은 ~/auth/~

bp_auth = Blueprint('auth_bp', # 별칭, 해당 블루프린트 밑에서 정의된 
                               # 라우트 및 함수를 url_for('main_bp.home')으로 지칭할때 사용
                    __name__,  # 고정
                    url_prefix='/auth', # 모든 URL앞에 /main이 추가된다
                    template_folder='../templates/auth', # html위치하는 폴더지정
                    static_folder='../static'       # 정적 데이터가 위치하는 폴더
                    )