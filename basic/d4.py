'''
    데이터베이스 접속후 쿼리 수행 + 파라미터 전달
'''
import pymysql as my
def select_login(uid,upw):
    connection = None
    try:
        connection = my.connect(host='localhost', #127.0.0.0 
                                #port= 3306,
                                user='root',
                                password='12341234',
                                database='ml_db',
                                # 조회 결과를 [ {} , {} , {} ] 로 변경 해줌
                                cursorclass=my.cursors.DictCursor
                                )    
        with connection.cursor() as cursor:
            sql = '''
                SELECT 
                    uid, `name`, regdate 
                FROM 
                    users
                WHERE
                    uid=%s
                AND
                    upw=%s;
                '''
            cursor.execute(sql,(uid,upw))
            row = cursor.fetchone()
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

if __name__ == '__main__':
    # d4 개발자의 테스트 코드
    # f5 개발자가 사용할때는 작동안함
    select_login('guest','1234')
