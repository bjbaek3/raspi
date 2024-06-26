import pymysql

db=pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')

cur = db.cursor()

cur.execute("INSERT INTO helloworld(yyyymmdd, msg) VALUES (NOW(), '한글메세지') ")

db.commit()

db.close()
 