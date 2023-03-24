'''
    데이터베이스 접속 후 쿼리 수행
'''
import pymysql as my

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
                uid='guest'
            AND
                upw='1234';
            '''
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row['name'])

except Exception as e:
    print('접속 오류', e)
else: 
    print('접속 문제 없음')
finally:
    if connection:
        connection.close()
