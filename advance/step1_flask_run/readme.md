# 어플리케이션 구동
    - flask 명령상 기본으로 찾는 파일(아래 파일들은 공종하면 의도하지 않은 것이 수행 될 수 있다)
        - 1개만 설정하는 것으로 기준
        - wsgi.py
        - app.py
        - 환경 변수에 지정된 파일(FLASK_APP=XXX)찾는다
    - 커스텀 설정
        - 1.환경 변수를 지정하고 실행 -> OS에 설정하거나  혹은 shell(맥/리눅스) or cmd(윈도우) 작성해서 구동
            - set FLASK_APP=start_app
            - flask run
        - 2.환경 변수 파일을 읽어서 처리
            - conda install python-dotenv -y
            - pip install python-dotenv
            - 파일 생성
                - env.config
                - start_app.py
            - 실행
                - flask -e ./env.config run
        3. 명령 수행시 옵션 제공
            - flask --app start_app run
            - flask --app start_app --debug run

# 실습
    - wsgi.py 파일 생성
    - 실행
        - flask run 
        ```
         * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        * Running on http://127.0.0.1:5000
        Press CTRL+C to quit
        ```