'''
    데이터베이스 접속후 쿼리 수행
'''
import pymysql as my

connection = None
try:
    # 1.접속
    connection = my.connect(host        ='localhost',  
                            #port        = 3306,       
                            user        ='root',       
                            password    ='12341234',     
                            database    = 'ml_db',
                            # 조회 결과는 [ {},{},{}...]형태로 추출된다
                            cursorclass =my.cursors.DictCursor
                            )
    with connection.cursor() as cursor:

     sql='''
         SELECT
            uid,`NAME`,regdate
        FROM
            users
        WHERE
            uid='guest'
        AND
            upw='1234';
     '''
    cursor.execute(sql)
    row = cursor.fetchone()
    # 5. 결과 확인 -> 딕셔너리 -> 이름만 추출하시오 -> 순서가 중요,인덱싱 -> '게스트'
    print(row['name'])
    pass
except Exception as e:
    print('접속 오류',e)
else:
    print('접속시 문제없음')
finally:
    # 2. 접속 종료(I/o)->close()
    if connection:
        connection.close()
    print('접속 종료 성공')
