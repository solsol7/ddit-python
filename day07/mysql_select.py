import pymysql
conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='python', db='python', charset='utf8')

#curs = conn.cursor()
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from emp"
curs.execute(sql)
result = curs.fetchall()
for record in result:
    print(record)

curs.close()
conn.close()