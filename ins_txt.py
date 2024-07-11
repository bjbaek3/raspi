import pymysql

db=pymysql.connect(host='oldmansea.synology.me', user='root', password='Fyeo2014!@#', db='oldman',charset='utf8')

cur = db.cursor()

#count = 0
#while (count < 100):

cur.execute("INSERT INTO helloworld(yyyymmdd, msg) VALUES (NOW(), '루프가 잘 작동 않함.') ")
db.commit()

# count= count + 1




db.close()
 